from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.student import Student as StudentModel
from app.models.group import Group as GroupModel
from app.schemas.student import Student

router = APIRouter()

@router.put("/{student_id}/group/{group_id}", response_model=Student)
def add_student_to_group(student_id: int, group_id: int, db: Session = Depends(get_db)):
    """添加学生到组"""
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    group = db.query(GroupModel).filter(GroupModel.id == group_id).first()
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    student.group_id = group_id
    db.commit()
    db.refresh(student)
    return student

@router.delete("/{student_id}/group", response_model=Student)
def remove_student_from_group(student_id: int, db: Session = Depends(get_db)):
    """从组中移除学生"""
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.group_id = None
    db.commit()
    db.refresh(student)
    return student

@router.put("/{student_id}/transfer/{new_group_id}", response_model=Student)
def transfer_student(student_id: int, new_group_id: int, db: Session = Depends(get_db)):
    """将学生转移到新组"""
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_group = db.query(GroupModel).filter(GroupModel.id == new_group_id).first()
    if new_group is None:
        raise HTTPException(status_code=404, detail="New group not found")
    
    student.group_id = new_group_id
    db.commit()
    db.refresh(student)
    return student