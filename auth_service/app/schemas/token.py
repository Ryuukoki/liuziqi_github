from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None
    email: Optional[str] = None


class TokenPayload(BaseModel):
    sub: str  # user_id or email
    exp: int  # expiration timestamp
    iat: int  # issued at timestamp
    type: str  # token type: access or refresh


class RefreshTokenRequest(BaseModel):
    refresh_token: str