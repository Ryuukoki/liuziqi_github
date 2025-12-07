"""
正方形类实现
"""
from shapes.base_shape import Shape


class Square(Shape):
    """正方形类"""
    
    def __init__(self, side: float):
        """
        初始化正方形
        
        Args:
            side: 正方形边长，必须为正数
        """
        if side <= 0:
            raise ValueError("边长必须为正数")
        self.side = side
    
    def area(self) -> float:
        """计算正方形面积"""
        return self.side ** 2
    
    def perimeter(self) -> float:
        """计算正方形周长"""
        return 4 * self.side
    
    def __repr__(self) -> str:
        return f"Square(side={self.side})"
    
    def get_diagonal(self) -> float:
        """获取正方形对角线长度"""
        return self.side * (2 ** 0.5)