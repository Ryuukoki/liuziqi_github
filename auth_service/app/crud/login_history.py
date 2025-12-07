# app/crud/login_history.py
from datetime import datetime
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from app.models import LoginHistory


async def create_login_history(db: AsyncSession, user_id: int, user_agent: str = None, ip_address: str = None) -> LoginHistory:
    """创建登录历史记录"""
    login_history = LoginHistory(
        user_id=user_id,
        user_agent=user_agent,
        ip_address=ip_address,
        login_time=datetime.utcnow()
    )
    db.add(login_history)
    await db.commit()
    await db.refresh(login_history)
    return login_history


async def get_user_login_history(db: AsyncSession, user_id: int, limit: int = 50) -> List[LoginHistory]:
    """获取用户登录历史"""
    result = await db.execute(
        select(LoginHistory)
        .where(LoginHistory.user_id == user_id)
        .order_by(desc(LoginHistory.login_time))
        .limit(limit)
    )
    return result.scalars().all()