"""
圆形类实现
"""
from shapes.base_shape import Shape
import math


class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius: float):
        """
        初始化圆形
        
        Args:
            radius: 圆半径，必须为正数
        """
        if radius <= 0:
            raise ValueError("半径必须为正数")
        self.radius = radius
    
    def area(self) -> float:
        """计算圆面积"""
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """计算圆周长（圆周）"""
        return 2 * math.pi * self.radius
    
    def circumference(self) -> float:
        """圆周的别名（与perimeter相同）"""
        return self.perimeter()
    
    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"
    
    def diameter(self) -> float:
        """获取直径"""
        return 2 * self.radius
    
    def sector_area(self, angle_degrees: float) -> float:
        """计算扇形面积
        
        Args:
            angle_degrees: 扇形角度（度）
            
        Returns:
            float: 扇形面积
        """
        if angle_degrees < 0 or angle_degrees > 360:
            raise ValueError("角度必须在0到360度之间")
        return (angle_degrees / 360) * self.area()