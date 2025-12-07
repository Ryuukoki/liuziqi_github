from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.database import get_db
from app.crud.user import update_user as crud_update_user, get_user_by_email
from app.crud.login_history import get_user_login_history
from app.schemas.user import UserUpdate, UserResponse
from app.api.dependencies import get_current_active_user

router = APIRouter()


@router.put("/user/update", response_model=UserResponse)
async def update_user(
    user_update: UserUpdate,
    current_user: dict = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    """
    更新用户信息
    - email: 新邮箱（可选）
    - password: 新密码（可选）
    """
    # 如果更新邮箱，检查是否已被其他用户使用
    if user_update.email and user_update.email != current_user.email:
        existing_user = await get_user_by_email(db, user_update.email)
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="邮箱已被其他用户使用",
            )
    
    # 更新用户信息
    updated_user = await crud_update_user(db, current_user, user_update)
    
    return updated_user


@router.get("/user/history")
async def get_login_history(
    current_user: dict = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
    limit: int = 50,
):
    """
    获取用户登录历史
    - limit: 返回记录数量限制（默认50）
    """
    history = await get_user_login_history(db, current_user.id, limit)
    
    # 格式化返回数据
    history_list = []
    for record in history:
        history_list.append({
            "id": record.id,
            "user_agent": record.user_agent,
            "ip_address": record.ip_address,
            "login_time": record.login_time.isoformat() if record.login_time else None,
        })
    
    return history_list


@router.get("/user/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: dict = Depends(get_current_active_user),
):
    """
    获取当前用户信息（可选功能）
    """
    return current_user


@router.post("/user/logout-all")
async def logout_all_devices(
    current_user: dict = Depends(get_current_active_user),
):
    """
    撤销用户所有设备的令牌（可选功能）
    """
    # 撤销用户的所有令牌
    from app.core.redis_client import redis_client
    success = await redis_client.revoke_all_user_tokens(current_user.id)
    
    if success:
        return {"message": "已从所有设备退出登录"}
    else:
        return {"message": "退出登录请求已处理，但令牌撤销可能未完全执行"}