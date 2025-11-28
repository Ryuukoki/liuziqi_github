# 删除这行，因为会造成循环导入
# Group.students = relationship("Student", back_populates="group")

# 只保留导入
from .group import Group
from .student import Student