"""
形状类的单元测试
"""
import unittest
import math
from shapes import Square, Rectangle, Triangle, Circle
from utils import GeometryCalculator


class TestShapes(unittest.TestCase):
    
    def test_square(self):
        """测试正方形类"""
        square = Square(5)
        
        # 测试面积
        self.assertEqual(square.area(), 25)
        
        # 测试周长
        self.assertEqual(square.perimeter(), 20)
        
        # 测试对角线
        self.assertAlmostEqual(square.get_diagonal(), 5 * math.sqrt(2))
        
        # 测试无效边长
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)
    
    def test_rectangle(self):
        """测试矩形类"""
        rectangle = Rectangle(4, 6)
        
        # 测试面积
        self.assertEqual(rectangle.area(), 24)
        
        # 测试周长
        self.assertEqual(rectangle.perimeter(), 20)
        
        # 测试是否为正方形
        self.assertFalse(rectangle.is_square())
        
        # 测试正方形矩形
        square_rect = Rectangle(5, 5)
        self.assertTrue(square_rect.is_square())
        
        # 测试对角线
        self.assertAlmostEqual(rectangle.get_diagonal(), math.sqrt(4**2 + 6**2))
        
        # 测试无效尺寸
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, -3)
    
    def test_triangle(self):
        """测试三角形类"""
        # 测试三边三角形
        triangle1 = Triangle(3, 4, 5)
        self.assertEqual(triangle1.area(), 6)  # 3-4-5三角形面积是6
        self.assertEqual(triangle1.perimeter(), 12)
        self.assertTrue(triangle1.is_right_triangle())
        
        # 测试底高三角形
        triangle2 = Triangle(base=5, height=4)
        self.assertEqual(triangle2.area(), 10)
        
        # 测试两边夹角三角形
        triangle3 = Triangle(side1=3, side2=4, angle=90)
        self.assertAlmostEqual(triangle3.area(), 6, places=5)
        
        # 测试等边三角形
        triangle4 = Triangle(3, 3, 3)
        self.assertTrue(triangle4.is_equilateral())
        
        # 测试无效三角形
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # 不能构成三角形
    
    def test_circle(self):
        """测试圆形类"""
        circle = Circle(3)
        
        # 测试面积
        self.assertAlmostEqual(circle.area(), math.pi * 9, places=5)
        
        # 测试周长
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * 3, places=5)
        
        # 测试直径
        self.assertEqual(circle.diameter(), 6)
        
        # 测试扇形面积
        self.assertAlmostEqual(circle.sector_area(90), circle.area() / 4, places=5)
        
        # 测试无效半径
        with self.assertRaises(ValueError):
            Circle(0)
    
    def test_comparisons(self):
        """测试形状比较"""
        square = Square(4)  # 面积=16
        circle = Circle(2)  # 面积≈12.57
        
        # 测试面积比较
        self.assertTrue(square.area_greater_than(circle))
        self.assertFalse(square.area_less_than(circle))
        
        # 测试周长比较
        self.assertTrue(square.perimeter_greater_than(circle))  # 16 > ~12.57
        self.assertFalse(square.perimeter_less_than(circle))
        
        # 测试相同面积的形状
        square2 = Square(4)
        self.assertFalse(square.area_greater_than(square2))
        self.assertFalse(square.area_less_than(square2))
    
    def test_geometry_calculator(self):
        """测试几何计算工具"""
        shapes = [
            Square(2),      # 面积=4
            Rectangle(3, 2),  # 面积=6
            Circle(1)       # 面积≈3.14
        ]
        
        calculator = GeometryCalculator()
        
        # 测试最大面积
        largest = calculator.get_largest_area(shapes)
        self.assertEqual(largest.area(), 6)  # 矩形面积最大
        
        # 测试最小周长
        smallest_perim = calculator.get_smallest_perimeter(shapes)
        self.assertAlmostEqual(smallest_perim.perimeter(), 2 * math.pi, places=5)
        
        # 测试总面积
        total_area = calculator.calculate_total_area(shapes)
        self.assertAlmostEqual(total_area, 4 + 6 + math.pi, places=5)
        
        # 测试空列表
        with self.assertRaises(ValueError):
            calculator.get_largest_area([])


def run_tests():
    """运行所有测试"""
    print("运行形状类测试...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShapes)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n所有测试通过!")
    else:
        print(f"\n测试失败: {len(result.failures)}个失败")


if __name__ == "__main__":
    run_tests()