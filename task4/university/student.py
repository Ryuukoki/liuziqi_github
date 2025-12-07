"""
学生类，继承自Person
"""
from typing import Optional, Union
from university.person import Person
from financial.scholarship import calculate_student_scholarship


class Student(Person):
    """学生类，继承自Person"""
    
    def __init__(self, first_name: str, last_name: str, age: int, 
                 group_number: str, average_score: float):
        """
        初始化学生
        
        Args:
            first_name: 名
            last_name: 姓
            age: 年龄
            group_number: 组号/学号
            average_score: 平均分（0-5）
        """
        super().__init__(first_name, last_name, age)
        
        self.group_number = group_number
        
        if not 0 <= average_score <= 5:
            raise ValueError("平均分必须在0到5之间")
        self.average_score = average_score
    
    def get_info(self) -> str:
        """获取学生信息（扩展父类方法）"""
        base_info = super().get_info()
        return f"{base_info}, 组号: {self.group_number}, 平均分: {self.average_score:.2f}"
    
    def get_scholarship(self) -> float:
        """获取奖学金金额"""
        return calculate_student_scholarship(self.average_score)
    
    def display_scholarship(self) -> None:
        """显示奖学金信息"""
        scholarship = self.get_scholarship()
        if scholarship > 0:
            print(f"{self.get_full_name()} 的奖学金: {scholarship:.0f}₽")
        else:
            print(f"{self.get_full_name()} 没有奖学金")
    
    def compare_scholarship(self, other: 'Student') -> dict:
        """与另一个学生比较奖学金
        
        Returns:
            dict: 包含比较结果的字典
        """
        my_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()
        
        return {
            '当前学生': self.get_full_name(),
            '另一学生': other.get_full_name(),
            '当前奖学金': my_scholarship,
            '另一奖学金': other_scholarship,
            '比较结果': {
                '当前更多': my_scholarship > other_scholarship,
                '当前更少': my_scholarship < other_scholarship,
                '相等': my_scholarship == other_scholarship
            }
        }
    
    def is_scholarship_greater(self, other: 'Student') -> bool:
        """检查当前学生的奖学金是否多于另一个学生"""
        return self.get_scholarship() > other.get_scholarship()
    
    def is_scholarship_less(self, other: 'Student') -> bool:
        """检查当前学生的奖学金是否少于另一个学生"""
        return self.get_scholarship() < other.get_scholarship()
    
    def __repr__(self) -> str:
        return (f"Student(first_name='{self.first_name}', last_name='{self.last_name}', "
                f"age={self.age}, group_number='{self.group_number}', "
                f"average_score={self.average_score})")
    
    def to_dict(self) -> dict:
        """将学生信息转换为字典"""
        return {
            'type': 'student',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'group_number': self.group_number,
            'average_score': self.average_score,
            'scholarship': self.get_scholarship()
        }