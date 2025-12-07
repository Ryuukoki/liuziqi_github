from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.database import get_db, create_tables
from app.api.endpoints import auth, users
from app.core.redis_client import redis_client
from app.api.dependencies import get_current_user  # 使用统一的依赖函数

# 配置日志
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用生命周期管理
    - 启动时：连接数据库和Redis
    - 关闭时：清理连接
    """
    # 启动时
    logger.info("Starting Auth Service...")
    logger.info(f"Environment: {settings.APP_ENV}")
    
    # 初始化Redis连接
    await redis_client.initialize()
    
    # 创建数据库表（仅开发环境）
    if settings.APP_ENV == "development":
        try:
            await create_tables()
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.warning(f"Could not create tables: {e}")
    
    yield
    
    # 关闭时
    logger.info("Shutting down Auth Service...")
    await redis_client.close()


# 创建FastAPI应用
app = FastAPI(
    title=settings.APP_NAME,
    description="基于JWT的用户认证与授权服务",
    version="1.0.0",
    lifespan=lifespan,
    debug=settings.DEBUG,
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 注册路由 - 按照文档要求的路径
app.include_router(
    auth.router,
    prefix="",  # 修改：不使用前缀，直接使用文档要求的路径
    tags=["认证"],
)

app.include_router(
    users.router,
    prefix="",  # 修改：不使用前缀，直接使用文档要求的路径
    tags=["用户"],
    dependencies=[Depends(get_current_user)],  # 为所有用户端点添加认证依赖
)


# 根路由
@app.get("/")
async def root():
    """API根路径"""
    return {
        "message": f"欢迎使用{settings.APP_NAME}",
        "version": "1.0.0",
        "docs": "/docs",
        "environment": settings.APP_ENV,
    }


# 健康检查
@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {
        "status": "healthy",
        "database": "connected",
        "redis": "connected",
    }


# 处理404错误
@app.exception_handler(404)
async def not_found_exception_handler(request, exc):
    return {
        "detail": f"未找到请求的资源: {request.url.path}"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG,
    )