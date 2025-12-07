"""
基础人类，包含个人信息
"""
from typing import Optional


class Person:
    """基础人类，包含姓名和年龄"""
    
    def __init__(self, first_name: str, last_name: str, age: int):
        """
        初始化人员信息
        
        Args:
            first_name: 名
            last_name: 姓
            age: 年龄
        """
        self.first_name = first_name
        self.last_name = last_name
        
        if age < 0 or age > 120:
            raise ValueError("年龄必须在0到120岁之间")
        self.age = age
    
    def get_full_name(self) -> str:
        """获取完整姓名"""
        return f"{self.first_name} {self.last_name}"
    
    def get_info(self) -> str:
        """获取个人信息"""
        return f"姓名: {self.get_full_name()}, 年龄: {self.age}"
    
    def display_info(self) -> None:
        """显示个人信息"""
        print(self.get_info())
    
    def __str__(self) -> str:
        return f"Person({self.get_full_name()}, {self.age}岁)"
    
    def __repr__(self) -> str:
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', age={self.age})"