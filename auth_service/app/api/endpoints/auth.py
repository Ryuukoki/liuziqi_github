from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr

from app.database import get_db
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.core.redis_client import redis_client
from app.crud.user import (
    get_user_by_email,
    create_user,
    authenticate_user,
    get_user_by_id,
)
from app.crud.login_history import create_login_history
from app.schemas.user import UserCreate, UserResponse
from app.schemas.token import Token, RefreshTokenRequest
from app.api.dependencies import (
    get_current_user,
    get_user_agent,
    get_client_ip,
    validate_refresh_token,
)

router = APIRouter()


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    用户注册
    - email: 用户邮箱（必须唯一）
    - password: 密码
    """
    # 检查邮箱是否已存在
    existing_user = await get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="邮箱已被注册",
        )
    
    # 创建新用户
    user_create = UserCreate(email=user_data.email, password=user_data.password)
    user = await create_user(db, user_create)
    
    return user


@router.post("/login", response_model=Token)
async def login(
    login_data: LoginRequest,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user_agent: str = Depends(get_user_agent),
    client_ip: str = Depends(get_client_ip),
):
    """
    用户登录
    - email: 用户邮箱
    - password: 密码
    返回access_token和refresh_token
    """
    # 验证用户凭证
    user = await authenticate_user(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="邮箱或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 创建令牌
    token_data = {"sub": str(user.id), "email": user.email}
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)
    
    # 记录登录历史
    await create_login_history(db, user.id, user_agent, client_ip)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh", response_model=Token)
async def refresh_token(
    token_data: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    刷新访问令牌
    - refresh_token: 刷新令牌
    返回新的access_token和refresh_token
    """
    refresh_token_value = token_data.refresh_token
    
    # 验证refresh_token
    user_id = await validate_refresh_token(refresh_token_value)
    
    # 获取用户信息
    user = await get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在",
        )
    
    # 将旧的refresh_token加入黑名单
    token_payload = decode_token(refresh_token_value)
    if token_payload and "exp" in token_payload:
        expires_at = datetime.utcfromtimestamp(token_payload["exp"])
        await redis_client.add_to_blacklist(refresh_token_value, user.id, expires_at)
    
    # 创建新的令牌
    new_token_data = {"sub": str(user.id), "email": user.email}
    new_access_token = create_access_token(new_token_data)
    new_refresh_token = create_refresh_token(new_token_data)
    
    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }


@router.post("/logout")
async def logout(
    request: Request,
    current_user: dict = Depends(get_current_user),
):
    """
    用户退出登录
    将当前用户的令牌加入黑名单
    """
    # 获取请求中的令牌
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        
        # 解码令牌以获取过期时间
        token_payload = decode_token(token)
        if token_payload and "exp" in token_payload:
            expires_at = datetime.utcfromtimestamp(token_payload["exp"])
            # 将令牌加入黑名单
            await redis_client.add_to_blacklist(token, current_user.id, expires_at)
    
    return {"message": "成功退出登录"}