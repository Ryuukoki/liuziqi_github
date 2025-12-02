"""
工具函数模块
"""

# 这里可以添加一些通用的工具函数
# 例如：日期处理、字符串处理、验证函数等

from datetime import datetime
from typing import Any, Dict


def format_datetime(dt: datetime) -> str:
    """格式化日期时间为字符串"""
    if dt:
        return dt.isoformat()
    return None


def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """清理字典中的None值"""
    return {k: v for k, v in data.items() if v is not None}


def mask_email(email: str) -> str:
    """掩码邮箱地址（保护隐私）"""
    if "@" in email:
        username, domain = email.split("@")
        if len(username) > 2:
            masked = username[0] + "*" * (len(username) - 2) + username[-1]
        else:
            masked = "*" * len(username)
        return f"{masked}@{domain}"
    return email


__all__ = ["format_datetime", "clean_dict", "mask_email"]