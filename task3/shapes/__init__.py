"""
形状模块的初始化文件
导出所有形状类，便于导入
"""
from .base_shape import Shape
from .square import Square
from .rectangle import Rectangle
from .triangle import Triangle
from .circle import Circle

__all__ = ['Shape', 'Square', 'Rectangle', 'Triangle', 'Circle']