"""
三角形类实现
支持三种三角形：通过三边长度、底和高、或两边和夹角
"""
from shapes.base_shape import Shape
import math


class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, *args, **kwargs):
        """
        初始化三角形，支持多种初始化方式：
        
        方式1: Triangle(a, b, c) - 通过三边长度
        方式2: Triangle(base=5, height=3) - 通过底和高
        方式3: Triangle(side1=3, side2=4, angle=90) - 通过两边和夹角（度）
        """
        if len(args) == 3:
            # 三边长度
            a, b, c = args
            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError("边长必须为正数")
            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError("三边长度不能构成三角形")
            self.a = a
            self.b = b
            self.c = c
            self._type = "三边"
        elif 'base' in kwargs and 'height' in kwargs:
            # 底和高
            base = kwargs['base']
            height = kwargs['height']
            if base <= 0 or height <= 0:
                raise ValueError("底和高必须为正数")
            self.base = base
            self.height = height
            self._type = "底高"
        elif 'side1' in kwargs and 'side2' in kwargs and 'angle' in kwargs:
            # 两边和夹角
            side1 = kwargs['side1']
            side2 = kwargs['side2']
            angle = kwargs['angle']
            if side1 <= 0 or side2 <= 0:
                raise ValueError("边长必须为正数")
            if angle <= 0 or angle >= 180:
                raise ValueError("夹角必须在0到180度之间")
            self.side1 = side1
            self.side2 = side2
            self.angle = math.radians(angle)  # 转换为弧度
            self._type = "两边夹角"
        else:
            raise ValueError("无效的初始化参数")
    
    def area(self) -> float:
        """计算三角形面积"""
        if self._type == "三边":
            # 使用海伦公式
            s = self.perimeter() / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        elif self._type == "底高":
            return 0.5 * self.base * self.height
        elif self._type == "两边夹角":
            return 0.5 * self.side1 * self.side2 * math.sin(self.angle)
        else:
            raise ValueError("未知的三角形类型")
    
    def perimeter(self) -> float:
        """计算三角形周长"""
        if self._type == "三边":
            return self.a + self.b + self.c
        elif self._type == "底高":
            # 假设为等腰三角形来计算周长
            # 等腰三角形的腰长 = sqrt((底/2)^2 + 高^2)
            leg = math.sqrt((self.base / 2) ** 2 + self.height ** 2)
            return self.base + 2 * leg
        elif self._type == "两边夹角":
            # 使用余弦定理计算第三边
            side3 = math.sqrt(self.side1**2 + self.side2**2 - 
                            2 * self.side1 * self.side2 * math.cos(self.angle))
            return self.side1 + self.side2 + side3
        else:
            raise ValueError("未知的三角形类型")
    
    def __repr__(self) -> str:
        if self._type == "三边":
            return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
        elif self._type == "底高":
            return f"Triangle(base={self.base}, height={self.height})"
        elif self._type == "两边夹角":
            return f"Triangle(side1={self.side1}, side2={self.side2}, angle={math.degrees(self.angle):.1f}°)"
    
    def is_right_triangle(self) -> bool:
        """检查是否为直角三角形（仅对三边类型有效）"""
        if self._type != "三边":
            return False
        
        sides = sorted([self.a, self.b, self.c])
        # 使用勾股定理检查
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)
    
    def is_equilateral(self) -> bool:
        """检查是否为等边三角形（仅对三边类型有效）"""
        if self._type != "三边":
            return False
        
        return math.isclose(self.a, self.b) and math.isclose(self.b, self.c)