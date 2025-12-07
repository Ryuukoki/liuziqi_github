"""
几何计算工具类
"""
from typing import List
from shapes.base_shape import Shape
from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle
from shapes.circle import Circle


class GeometryCalculator:
    """几何计算工具类"""
    
    @staticmethod
    def compare_shapes(shape1: Shape, shape2: Shape) -> dict:
        """比较两个形状的面积和周长"""
        return shape1.compare_with(shape2)
    
    @staticmethod
    def get_largest_area(shapes: List[Shape]) -> Shape:
        """从形状列表中找出面积最大的形状"""
        if not shapes:
            raise ValueError("形状列表不能为空")
        return max(shapes, key=lambda s: s.area())
    
    @staticmethod
    def get_smallest_perimeter(shapes: List[Shape]) -> Shape:
        """从形状列表中找出周长最小的形状"""
        if not shapes:
            raise ValueError("形状列表不能为空")
        return min(shapes, key=lambda s: s.perimeter())
    
    @staticmethod
    def calculate_total_area(shapes: List[Shape]) -> float:
        """计算所有形状的总面积"""
        return sum(shape.area() for shape in shapes)
    
    @staticmethod
    def calculate_total_perimeter(shapes: List[Shape]) -> float:
        """计算所有形状的总周长"""
        return sum(shape.perimeter() for shape in shapes)
    
    @staticmethod
    def create_shape_from_dict(shape_data: dict) -> Shape:
        """从字典数据创建形状对象
        
        Args:
            shape_data: 包含形状类型和参数的字典
                例如: {'type': 'square', 'side': 5}
                     {'type': 'circle', 'radius': 3}
        """
        shape_type = shape_data.get('type', '').lower()
        
        if shape_type == 'square':
            return Square(shape_data['side'])
        elif shape_type == 'rectangle':
            return Rectangle(shape_data['width'], shape_data['height'])
        elif shape_type == 'triangle':
            # 支持多种三角形创建方式
            if 'base' in shape_data and 'height' in shape_data:
                return Triangle(base=shape_data['base'], height=shape_data['height'])
            elif 'a' in shape_data and 'b' in shape_data and 'c' in shape_data:
                return Triangle(shape_data['a'], shape_data['b'], shape_data['c'])
            elif 'side1' in shape_data and 'side2' in shape_data and 'angle' in shape_data:
                return Triangle(side1=shape_data['side1'], 
                               side2=shape_data['side2'], 
                               angle=shape_data['angle'])
            else:
                raise ValueError("无效的三角形参数")
        elif shape_type == 'circle':
            return Circle(shape_data['radius'])
        else:
            raise ValueError(f"未知的形状类型: {shape_type}")