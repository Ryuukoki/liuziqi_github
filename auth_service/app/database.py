# app/database.py
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool
from app.config import settings

# 创建异步数据库引擎 - 使用 settings.DATABASE_URL
engine = create_async_engine(
    settings.DATABASE_URL,  # 注意：settings.DATABASE_URL 现在是字符串
    echo=settings.DEBUG,  # 调试模式下输出SQL语句
    pool_pre_ping=True,   # 每次连接前检查连接是否有效
    pool_recycle=3600,    # 1小时后回收连接
)

# 创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# 声明基类
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    获取数据库会话的依赖函数
    使用示例：db: AsyncSession = Depends(get_db)
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def create_tables():
    """创建所有数据库表（仅用于开发）"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    """删除所有数据库表（仅用于测试）"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)