from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.group import Group as GroupModel
from app.models.student import Student as StudentModel
from app.schemas.group import Group, GroupCreate
from app.schemas.student import Student

router = APIRouter()

@router.post("/", response_model=Group)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = GroupModel(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.get("/{group_id}", response_model=Group)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(GroupModel).filter(GroupModel.id == group_id).first()
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

@router.get("/", response_model=List[Group])
def get_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """获取组列表"""
    groups = db.query(GroupModel).offset(skip).limit(limit).all()
    return groups

@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    """删除组"""
    group = db.query(GroupModel).filter(GroupModel.id == group_id).first()
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # 检查组中是否有学生
    students_in_group = db.query(StudentModel).filter(StudentModel.group_id == group_id).count()
    if students_in_group > 0:
        raise HTTPException(
            status_code=400, 
            detail=f"Cannot delete group with {students_in_group} students. Remove students first."
        )
    
    db.delete(group)
    db.commit()
    return {"message": "Group deleted successfully"}

@router.get("/{group_id}/students", response_model=List[Student])
def get_students_in_group(group_id: int, db: Session = Depends(get_db)):
    """获取组中的所有学生"""
    # 先检查组是否存在
    group = db.query(GroupModel).filter(GroupModel.id == group_id).first()
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    students = db.query(StudentModel).filter(StudentModel.group_id == group_id).all()
    return students