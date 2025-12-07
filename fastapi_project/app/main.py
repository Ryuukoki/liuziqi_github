from fastapi import FastAPI
from app.db import create_tables
from app.api import students, groups, student_groups

# 创建数据库表
create_tables()

app = FastAPI(title="Students API", version="1.0.0")

# 包含路由
app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])
app.include_router(student_groups.router, prefix="/students", tags=["student-groups"])

@app.get("/")
async def root():
    return {"message": "Students API is running"}