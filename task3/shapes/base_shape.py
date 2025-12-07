"""
基础形状抽象类
定义了所有形状的通用接口和方法
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """抽象基类，定义所有形状的接口"""
    
    @abstractmethod
    def area(self) -> float:
        """计算形状的面积"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """计算形状的周长"""
        pass
    
    def area_greater_than(self, other: 'Shape') -> bool:
        """比较当前形状的面积是否大于另一个形状
        
        Args:
            other: 要比较的另一个形状对象
            
        Returns:
            bool: True如果当前形状面积更大，否则False
        """
        if not isinstance(other, Shape):
            raise TypeError("只能与其他Shape对象比较")
        return self.area() > other.area()
    
    def area_less_than(self, other: 'Shape') -> bool:
        """比较当前形状的面积是否小于另一个形状
        
        Args:
            other: 要比较的另一个形状对象
            
        Returns:
            bool: True如果当前形状面积更小，否则False
        """
        if not isinstance(other, Shape):
            raise TypeError("只能与其他Shape对象比较")
        return self.area() < other.area()
    
    def perimeter_greater_than(self, other: 'Shape') -> bool:
        """比较当前形状的周长是否大于另一个形状
        
        Args:
            other: 要比较的另一个形状对象
            
        Returns:
            bool: True如果当前形状周长更大，否则False
        """
        if not isinstance(other, Shape):
            raise TypeError("只能与其他Shape对象比较")
        return self.perimeter() > other.perimeter()
    
    def perimeter_less_than(self, other: 'Shape') -> bool:
        """比较当前形状的周长是否小于另一个形状
        
        Args:
            other: 要比较的另一个形状对象
            
        Returns:
            bool: True如果当前形状周长更小，否则False
        """
        if not isinstance(other, Shape):
            raise TypeError("只能与其他Shape对象比较")
        return self.perimeter() < other.perimeter()
    
    def __str__(self) -> str:
        """返回形状的字符串表示"""
        return f"{self.__class__.__name__}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"
    
    def compare_with(self, other: 'Shape') -> dict:
        """与另一个形状进行完整比较
        
        Returns:
            dict: 包含面积和周长比较结果的字典
        """
        return {
            '面积比较': {
                '当前形状': self.area(),
                '另一形状': other.area(),
                '当前更大': self.area_greater_than(other),
                '当前更小': self.area_less_than(other)
            },
            '周长比较': {
                '当前形状': self.perimeter(),
                '另一形状': other.perimeter(),
                '当前更大': self.perimeter_greater_than(other),
                '当前更小': self.perimeter_less_than(other)
            }
        }