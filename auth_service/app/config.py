# app/config.py
import os
from typing import Optional

class Settings:
    """应用配置类（简化版）"""
    
    def __init__(self):
        # 应用配置
        self.APP_NAME = "Auth Service"
        self.APP_ENV = os.getenv("APP_ENV", "development")
        self.APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
        self.APP_PORT = int(os.getenv("APP_PORT", "8000"))
        self.DEBUG = self.APP_ENV == "development"
        
        # 数据库配置
        self.POSTGRES_USER = os.getenv("POSTGRES_USER", "auth_user")
        self.POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "auth_password")
        self.POSTGRES_DB = os.getenv("POSTGRES_DB", "auth_db")
        self.POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
        self.POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
        self.DATABASE_URL = f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        
        # Redis配置
        self.REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
        self.REDIS_HOST = os.getenv("REDIS_HOST", "redis")
        self.REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
        self.REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)  # 添加这行
        
        # JWT配置
        self.SECRET_KEY = os.getenv("SECRET_KEY", "biduahd983hbcancc3qc0")
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
        self.REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
        
        # CORS配置
        self.CORS_ORIGINS = ["*"]
        
        # 打印配置（仅开发环境）
        if self.DEBUG:
            print(f"配置加载完成：APP_ENV={self.APP_ENV}, DATABASE_URL={self.DATABASE_URL}")


# 创建全局配置实例
settings = Settings()