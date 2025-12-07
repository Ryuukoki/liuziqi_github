"""
矩形类实现
"""
from shapes.base_shape import Shape


class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width: float, height: float):
        """
        初始化矩形
        
        Args:
            width: 矩形宽度，必须为正数
            height: 矩形高度，必须为正数
        """
        if width <= 0 or height <= 0:
            raise ValueError("宽度和高度必须为正数")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """计算矩形面积"""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """计算矩形周长"""
        return 2 * (self.width + self.height)
    
    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def is_square(self) -> bool:
        """检查矩形是否为正方形"""
        return self.width == self.height
    
    def get_diagonal(self) -> float:
        """获取矩形对角线长度"""
        return (self.width ** 2 + self.height ** 2) ** 0.5