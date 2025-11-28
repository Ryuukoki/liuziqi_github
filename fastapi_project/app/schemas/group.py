from pydantic import BaseModel
from typing import List, Optional

class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    
    class Config:
        from_attributes = True

class GroupWithStudents(Group):
    students: List['Student'] = []