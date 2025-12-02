import redis.asyncio as redis
import json
from datetime import datetime, timedelta
from typing import Optional, Any
from app.config import settings


class RedisClient:
    """Redis客户端管理类"""
    
    def __init__(self):
        self.redis_client: Optional[redis.Redis] = None
    
    async def initialize(self):
        """初始化Redis连接"""
        try:
            self.redis_client = redis.from_url(
                str(settings.REDIS_URL),
                password=settings.REDIS_PASSWORD,
                encoding="utf-8",
                decode_responses=True,
            )
            
            # 测试连接
            await self.redis_client.ping()
            print("Redis连接成功")
        except Exception as e:
            print(f"Redis连接失败: {e}")
            self.redis_client = None
    
    async def close(self):
        """关闭Redis连接"""
        if self.redis_client:
            await self.redis_client.close()
            self.redis_client = None
    
    async def set(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """设置键值对"""
        if not self.redis_client:
            return False
        
        try:
            # 如果值不是字符串，转换为JSON字符串
            if not isinstance(value, str):
                value = json.dumps(value)
            
            if expire:
                await self.redis_client.setex(key, expire, value)
            else:
                await self.redis_client.set(key, value)
            
            return True
        except Exception:
            return False
    
    async def get(self, key: str) -> Optional[Any]:
        """获取键值"""
        if not self.redis_client:
            return None
        
        try:
            value = await self.redis_client.get(key)
            if value is None:
                return None
            
            # 尝试解析为JSON
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        except Exception:
            return None
    
    async def delete(self, key: str) -> bool:
        """删除键"""
        if not self.redis_client:
            return False
        
        try:
            result = await self.redis_client.delete(key)
            return result > 0
        except Exception:
            return False
    
    async def exists(self, key: str) -> bool:
        """检查键是否存在"""
        if not self.redis_client:
            return False
        
        try:
            result = await self.redis_client.exists(key)
            return result > 0
        except Exception:
            return False
    
    # ========== 令牌黑名单相关方法 ==========
    
    async def add_to_blacklist(self, token: str, user_id: int, expires_at: datetime) -> bool:
        """将令牌添加到黑名单"""
        if not self.redis_client:
            return False
        
        try:
            # 计算过期时间（秒）
            now = datetime.utcnow()
            expire_seconds = int((expires_at - now).total_seconds())
            
            if expire_seconds <= 0:
                return False
            
            # 存储令牌信息
            token_info = {
                "user_id": user_id,
                "expires_at": expires_at.isoformat(),
                "blacklisted_at": now.isoformat(),
            }
            
            # 使用令牌作为键，存储到Redis并设置过期时间
            key = f"blacklist:token:{token}"
            await self.redis_client.setex(
                key,
                expire_seconds,
                json.dumps(token_info),
            )
            
            # 同时为用户存储令牌列表（用于批量撤销）
            user_key = f"user:blacklisted_tokens:{user_id}"
            await self.redis_client.sadd(user_key, token)
            
            # 为用户令牌集合设置过期时间（比最晚的令牌晚一些）
            await self.redis_client.expire(user_key, expire_seconds + 3600)
            
            return True
        except Exception as e:
            print(f"添加到黑名单失败: {e}")
            return False
    
    async def is_token_blacklisted(self, token: str) -> bool:
        """检查令牌是否在黑名单中"""
        if not self.redis_client:
            return False
        
        try:
            key = f"blacklist:token:{token}"
            return await self.redis_client.exists(key) > 0
        except Exception:
            return False
    
    async def revoke_all_user_tokens(self, user_id: int) -> bool:
        """撤销用户的所有令牌"""
        if not self.redis_client:
            return False
        
        try:
            # 获取用户的所有黑名单令牌
            user_key = f"user:blacklisted_tokens:{user_id}"
            tokens = await self.redis_client.smembers(user_key)
            
            # 删除所有令牌
            for token in tokens:
                key = f"blacklist:token:{token}"
                await self.redis_client.delete(key)
            
            # 删除用户令牌集合
            await self.redis_client.delete(user_key)
            
            return True
        except Exception:
            return False


# 创建全局Redis客户端实例
redis_client = RedisClient()