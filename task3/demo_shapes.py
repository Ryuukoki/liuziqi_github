"""
形状类的演示程序
"""
from shapes import Square, Rectangle, Triangle, Circle
from utils import GeometryCalculator


def demonstrate_basic_shapes():
    """演示基本形状的创建和计算"""
    print("=" * 60)
    print("基本形状演示")
    print("=" * 60)
    
    # 创建各种形状
    square = Square(5)
    rectangle = Rectangle(4, 6)
    triangle1 = Triangle(3, 4, 5)  # 三边长度
    triangle2 = Triangle(base=5, height=4)  # 底和高
    triangle3 = Triangle(side1=3, side2=4, angle=90)  # 两边和夹角
    circle = Circle(3)
    
    shapes = [square, rectangle, triangle1, triangle2, triangle3, circle]
    
    # 显示每个形状的信息
    for shape in shapes:
        print(f"\n{shape}")
        print(f"  面积: {shape.area():.2f}")
        print(f"  周长: {shape.perimeter():.2f}")
    
    return shapes


def demonstrate_comparisons():
    """演示形状比较"""
    print("\n" + "=" * 60)
    print("形状比较演示")
    print("=" * 60)
    
    square = Square(5)      # 面积=25, 周长=20
    circle = Circle(3)      # 面积≈28.27, 周长≈18.85
    rectangle = Rectangle(4, 6)  # 面积=24, 周长=20
    
    print(f"\n正方形 vs 圆形:")
    comparison = square.compare_with(circle)
    print(f"  面积: 正方形({square.area():.2f}) {'>' if square.area_greater_than(circle) else '<'} 圆形({circle.area():.2f})")
    print(f"  周长: 正方形({square.perimeter():.2f}) {'>' if square.perimeter_greater_than(circle) else '<'} 圆形({circle.perimeter():.2f})")
    
    print(f"\n正方形 vs 矩形:")
    print(f"  面积: 正方形({square.area():.2f}) {'>' if square.area_greater_than(rectangle) else '<'} 矩形({rectangle.area():.2f})")
    print(f"  周长: 正方形({square.perimeter():.2f}) {'=' if square.perimeter() == rectangle.perimeter() else '≠'} 矩形({rectangle.perimeter():.2f})")
    
    # 更多详细比较
    print(f"\n详细比较结果:")
    comp_result = GeometryCalculator.compare_shapes(square, rectangle)
    for key, value in comp_result.items():
        print(f"  {key}:")
        for sub_key, sub_value in value.items():
            print(f"    {sub_key}: {sub_value}")


def demonstrate_geometry_calculator():
    """演示几何计算工具"""
    print("\n" + "=" * 60)
    print("几何计算工具演示")
    print("=" * 60)
    
    # 创建一组形状
    shapes = [
        Square(4),          # 面积=16
        Rectangle(3, 5),    # 面积=15
        Triangle(3, 4, 5),  # 面积=6
        Circle(2)           # 面积≈12.57
    ]
    
    print(f"\n形状列表:")
    for i, shape in enumerate(shapes, 1):
        print(f"  {i}. {shape.__class__.__name__}: 面积={shape.area():.2f}, 周长={shape.perimeter():.2f}")
    
    # 使用工具类进行计算
    calculator = GeometryCalculator()
    
    largest = calculator.get_largest_area(shapes)
    smallest_perim = calculator.get_smallest_perimeter(shapes)
    total_area = calculator.calculate_total_area(shapes)
    total_perimeter = calculator.calculate_total_perimeter(shapes)
    
    print(f"\n几何计算结果:")
    print(f"  面积最大的形状: {largest.__class__.__name__} (面积={largest.area():.2f})")
    print(f"  周长最小的形状: {smallest_perim.__class__.__name__} (周长={smallest_perim.perimeter():.2f})")
    print(f"  总面积: {total_area:.2f}")
    print(f"  总周长: {total_perimeter:.2f}")


def demonstrate_special_methods():
    """演示形状的特殊方法"""
    print("\n" + "=" * 60)
    print("特殊方法演示")
    print("=" * 60)
    
    square = Square(5)
    rectangle = Rectangle(5, 5)  # 这也是一个正方形
    triangle = Triangle(3, 4, 5)
    circle = Circle(3)
    
    print(f"\n正方形:")
    print(f"  对角线: {square.get_diagonal():.2f}")
    
    print(f"\n矩形:")
    print(f"  是否为正方形: {rectangle.is_square()}")
    print(f"  对角线: {rectangle.get_diagonal():.2f}")
    
    print(f"\n三角形 (3-4-5):")
    print(f"  是否为直角三角形: {triangle.is_right_triangle()}")
    print(f"  是否为等边三角形: {triangle.is_equilateral()}")
    
    print(f"\n圆形:")
    print(f"  直径: {circle.diameter():.2f}")
    print(f"  90°扇形面积: {circle.sector_area(90):.2f}")


def interactive_demo():
    """交互式演示"""
    print("\n" + "=" * 60)
    print("交互式形状创建")
    print("=" * 60)
    
    while True:
        print("\n选择要创建的形状:")
        print("1. 正方形")
        print("2. 矩形")
        print("3. 三角形")
        print("4. 圆形")
        print("5. 返回主菜单")
        
        choice = input("请输入选择 (1-5): ")
        
        if choice == '1':
            side = float(input("请输入正方形边长: "))
            try:
                square = Square(side)
                print(f"创建成功: {square}")
                print(f"面积: {square.area():.2f}, 周长: {square.perimeter():.2f}")
            except ValueError as e:
                print(f"错误: {e}")
        
        elif choice == '2':
            width = float(input("请输入矩形宽度: "))
            height = float(input("请输入矩形高度: "))
            try:
                rectangle = Rectangle(width, height)
                print(f"创建成功: {rectangle}")
                print(f"面积: {rectangle.area():.2f}, 周长: {rectangle.perimeter():.2f}")
            except ValueError as e:
                print(f"错误: {e}")
        
        elif choice == '3':
            print("选择三角形创建方式:")
            print("1. 通过三边长度")
            print("2. 通过底和高")
            print("3. 通过两边和夹角")
            
            tri_choice = input("请输入选择 (1-3): ")
            
            if tri_choice == '1':
                a = float(input("请输入边a长度: "))
                b = float(input("请输入边b长度: "))
                c = float(input("请输入边c长度: "))
                try:
                    triangle = Triangle(a, b, c)
                    print(f"创建成功: {triangle}")
                    print(f"面积: {triangle.area():.2f}, 周长: {triangle.perimeter():.2f}")
                except ValueError as e:
                    print(f"错误: {e}")
            
            elif tri_choice == '2':
                base = float(input("请输入底边长度: "))
                height = float(input("请输入高度: "))
                try:
                    triangle = Triangle(base=base, height=height)
                    print(f"创建成功: {triangle}")
                    print(f"面积: {triangle.area():.2f}, 周长: {triangle.perimeter():.2f}")
                except ValueError as e:
                    print(f"错误: {e}")
            
            elif tri_choice == '3':
                side1 = float(input("请输入第一条边长度: "))
                side2 = float(input("请输入第二条边长度: "))
                angle = float(input("请输入夹角角度(度): "))
                try:
                    triangle = Triangle(side1=side1, side2=side2, angle=angle)
                    print(f"创建成功: {triangle}")
                    print(f"面积: {triangle.area():.2f}, 周长: {triangle.perimeter():.2f}")
                except ValueError as e:
                    print(f"错误: {e}")
        
        elif choice == '4':
            radius = float(input("请输入圆半径: "))
            try:
                circle = Circle(radius)
                print(f"创建成功: {circle}")
                print(f"面积: {circle.area():.2f}, 周长: {circle.perimeter():.2f}")
            except ValueError as e:
                print(f"错误: {e}")
        
        elif choice == '5':
            break
        
        else:
            print("无效选择，请重试")


def main():
    """主函数"""
    print("形状类层次结构演示程序")
    print("=" * 60)
    
    while True:
        print("\n请选择演示模式:")
        print("1. 基本形状演示")
        print("2. 形状比较演示")
        print("3. 几何计算工具演示")
        print("4. 特殊方法演示")
        print("5. 交互式形状创建")
        print("6. 退出")
        
        choice = input("\n请输入选择 (1-6): ")
        
        if choice == '1':
            demonstrate_basic_shapes()
        elif choice == '2':
            demonstrate_comparisons()
        elif choice == '3':
            demonstrate_geometry_calculator()
        elif choice == '4':
            demonstrate_special_methods()
        elif choice == '5':
            interactive_demo()
        elif choice == '6':
            print("再见!")
            break
        else:
            print("无效选择，请重试")


if __name__ == "__main__":
    main()