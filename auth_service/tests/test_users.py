import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_update_user():
    """测试更新用户信息"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 注册用户
        await ac.post("/api/register", json={
            "email": "update_test@example.com",
            "password": "TestPassword123"
        })
        
        # 登录获取令牌
        login_response = await ac.post("/api/login", json={
            "email": "update_test@example.com",
            "password": "TestPassword123"
        })
        
        access_token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # 测试更新邮箱
        response = await ac.put("/api/user/update", json={
            "email": "updated_email@example.com"
        }, headers=headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "updated_email@example.com"
        
        # 测试更新密码
        response = await ac.put("/api/user/update", json={
            "password": "NewPassword123"
        }, headers=headers)
        
        assert response.status_code == 200
        
        # 用新密码登录
        login_response = await ac.post("/api/login", json={
            "email": "updated_email@example.com",
            "password": "NewPassword123"
        })
        
        assert login_response.status_code == 200


@pytest.mark.asyncio
async def test_login_history():
    """测试获取登录历史"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 注册用户
        await ac.post("/api/register", json={
            "email": "history_test@example.com",
            "password": "TestPassword123"
        })
        
        # 登录几次
        for _ in range(3):
            login_response = await ac.post("/api/login", json={
                "email": "history_test@example.com",
                "password": "TestPassword123"
            })
            access_token = login_response.json()["access_token"]
        
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # 获取登录历史
        response = await ac.get("/api/user/history", headers=headers)
        
        assert response.status_code == 200
        history = response.json()
        assert isinstance(history, list)
        assert len(history) >= 3  # 至少3次登录记录


@pytest.mark.asyncio
async def test_logout():
    """测试退出登录"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 注册用户
        await ac.post("/api/register", json={
            "email": "logout_test@example.com",
            "password": "TestPassword123"
        })
        
        # 登录获取令牌
        login_response = await ac.post("/api/login", json={
            "email": "logout_test@example.com",
            "password": "TestPassword123"
        })
        
        access_token = login_response.json()["access_token"]
        refresh_token = login_response.json()["refresh_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # 测试退出登录
        response = await ac.post("/api/logout", headers=headers)
        assert response.status_code == 200
        
        # 验证令牌已失效（尝试访问受保护端点）
        response = await ac.get("/api/user/history", headers=headers)
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_unauthenticated_access():
    """测试未认证访问"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 测试无令牌访问受保护端点
        response = await ac.get("/api/user/history")
        assert response.status_code == 401
        
        # 测试无效令牌访问
        headers = {"Authorization": "Bearer invalid_token"}
        response = await ac.get("/api/user/history", headers=headers)
        assert response.status_code == 401