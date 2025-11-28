from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    group_id: Optional[int] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    group_id: Optional[int] = None

class Student(StudentBase):
    id: int
    group_id: Optional[int]
    
    class Config:
        from_attributes = True