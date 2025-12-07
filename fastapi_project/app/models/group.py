from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # 添加这行
from app.db.session import Base

class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    
    # 在这里定义关系
    students = relationship("Student", back_populates="group")