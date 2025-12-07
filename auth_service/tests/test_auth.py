import pytest
from httpx import AsyncClient
from app.main import app
from app.config import settings


@pytest.mark.asyncio
async def test_register_user():
    """测试用户注册"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 测试成功注册
        response = await ac.post("/api/register", json={
            "email": "test@example.com",
            "password": "TestPassword123"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["email"] == "test@example.com"
        
        # 测试重复注册
        response = await ac.post("/api/register", json={
            "email": "test@example.com",
            "password": "AnotherPassword123"
        })
        
        assert response.status_code == 400
        assert "email already registered" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_login():
    """测试用户登录"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 先注册用户
        await ac.post("/api/register", json={
            "email": "login_test@example.com",
            "password": "TestPassword123"
        })
        
        # 测试成功登录
        response = await ac.post("/api/login", json={
            "email": "login_test@example.com",
            "password": "TestPassword123"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"
        
        # 测试错误密码
        response = await ac.post("/api/login", json={
            "email": "login_test@example.com",
            "password": "WrongPassword"
        })
        
        assert response.status_code == 401
        assert "invalid credentials" in response.json()["detail"].lower()
        
        # 测试不存在的用户
        response = await ac.post("/api/login", json={
            "email": "nonexistent@example.com",
            "password": "SomePassword"
        })
        
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_refresh_token():
    """测试刷新令牌"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 先注册并登录获取refresh_token
        await ac.post("/api/register", json={
            "email": "refresh_test@example.com",
            "password": "TestPassword123"
        })
        
        login_response = await ac.post("/api/login", json={
            "email": "refresh_test@example.com",
            "password": "TestPassword123"
        })
        
        refresh_token = login_response.json()["refresh_token"]
        
        # 测试刷新令牌
        response = await ac.post("/api/refresh", json={
            "refresh_token": refresh_token
        })
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data  # 应该返回新的refresh_token
        
        # 测试无效的refresh_token
        response = await ac.post("/api/refresh", json={
            "refresh_token": "invalid_token"
        })
        
        assert response.status_code == 401