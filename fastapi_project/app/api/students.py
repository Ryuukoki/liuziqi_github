from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.student import Student as StudentModel
from app.schemas.student import Student, StudentCreate, StudentUpdate

router = APIRouter()

@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # 检查邮箱是否已存在
    db_student = db.query(StudentModel).filter(StudentModel.email == student.email).first()
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_student = StudentModel(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=List[Student])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """获取学生列表"""
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return students

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """删除学生"""
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student_update: StudentUpdate, db: Session = Depends(get_db)):
    """更新学生信息（用于添加/移除/转移组）"""
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # 更新字段
    update_data = student_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_student, field, value)
    
    db.commit()
    db.refresh(db_student)
    return db_student