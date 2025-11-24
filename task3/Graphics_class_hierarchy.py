import math
from abc import ABC, abstractmethod
from typing import Union

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def area_larger_than(self, other: 'Shape') -> bool:
        
        return self.area() > other.area()
    
    def area_smaller_than(self, other: 'Shape') -> bool:
        
        return self.area() < other.area()
    
    def perimeter_larger_than(self, other: 'Shape') -> bool:
        
        return self.perimeter() > other.perimeter()
    
    def perimeter_smaller_than(self, other: 'Shape') -> bool:
        
        return self.perimeter() < other.perimeter()
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(площадь={self.area():.2f}, периметр={self.perimeter():.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Square(Shape):
    
    def __init__(self, side: float):
        
        if side <= 0:
            raise ValueError("Длина стороны должна быть больше 0")
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2
    
    def perimeter(self) -> float:
        return 4 * self.side
    
    def __str__(self) -> str:
        return f"Квадрат(сторона={self.side}, площадь={self.area():.2f}, периметр={self.perimeter():.2f})"


class Rectangle(Shape):
    
    def __init__(self, length: float, width: float):
        
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть больше 0")
        self.length = length
        self.width = width
    
    def area(self) -> float:
        return self.length * self.width
    
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
    
    def __str__(self) -> str:
        return f"Прямоугольник(длина={self.length}, ширина={self.width}, площадь={self.area():.2f}, периметр={self.perimeter():.2f})"


class Triangle(Shape):
    
    def __init__(self, a: float, b: float, c: float):
        
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длины сторон треугольника должны быть больше 0")
        
        # Проверка неравенства треугольника
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Указанные длины сторон не могут образовать действительный треугольник")
        
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        s = self.perimeter() / 2  # полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def is_equilateral(self) -> bool:
        return math.isclose(self.a, self.b) and math.isclose(self.b, self.c)
    
    def is_isosceles(self) -> bool:
        return (math.isclose(self.a, self.b) or 
                math.isclose(self.b, self.c) or 
                math.isclose(self.a, self.c))
    
    def is_right_triangle(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2]**2, sides[0]**2 + sides[1]**2)
    
    def __str__(self) -> str:
        triangle_type = []
        if self.is_equilateral():
            triangle_type.append("равносторонний ")
        elif self.is_isosceles():
            triangle_type.append("равнобедренный ")
        if self.is_right_triangle():
            triangle_type.append("прямоугольный ")
        
        type_str = "".join(triangle_type) if triangle_type else "обычный "
        return f"{type_str}треугольник(стороны={self.a},{self.b},{self.c}, площадь={self.area():.2f}, периметр={self.perimeter():.2f})"


class Circle(Shape):
    
    def __init__(self, radius: float):
        
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def circumference(self) -> float:
        return self.perimeter()
    
    def __str__(self) -> str:
        return f"Круг(радиус={self.radius}, площадь={self.area():.2f}, периметр={self.perimeter():.2f})"


def demonstrate_shapes():
    print("Задача 3: Демонстрация иерархии классов фигур")
    print("=" * 60)
    
    # Создаем экземпляры различных фигур
    shapes = [
        Square(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Triangle(5, 5, 5),  # равносторонний треугольник
        Triangle(5, 5, 7),  # равнобедренный треугольник
        Circle(3)
    ]
    
    # Отображаем информацию о всех фигурах
    print("Созданные фигуры:")
    print("-" * 40)
    for shape in shapes:
        print(f"  {shape}")
    print()
    
    # Демонстрация сравнения площадей
    print("Сравнение площадей:")
    print("-" * 40)
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            shape1 = shapes[i]
            shape2 = shapes[j]
            if shape1.area_larger_than(shape2):
                print(f"  Площадь {shape1.__class__.__name__} > Площадь {shape2.__class__.__name__}")
            else:
                print(f"  Площадь {shape1.__class__.__name__} < Площадь {shape2.__class__.__name__}")
    print()
    
    # Демонстрация сравнения периметров
    print("Сравнение периметров:")
    print("-" * 40)
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            shape1 = shapes[i]
            shape2 = shapes[j]
            if shape1.perimeter_larger_than(shape2):
                print(f"  Периметр {shape1.__class__.__name__} > Периметр {shape2.__class__.__name__}")
            else:
                print(f"  Периметр {shape1.__class__.__name__} < Периметр {shape2.__class__.__name__}")
    print()


def area_comparison_matrix():
    print("Матрица сравнения площадей:")
    print("-" * 40)
    
    shapes = [
        Square(4),      # площадь 16
        Rectangle(3, 5), # площадь 15
        Triangle(6, 8, 10), # площадь 24
        Circle(2)       # площадь около 12.57
    ]
    
    shape_names = [s.__class__.__name__ for s in shapes]
    
    # Печатаем заголовок таблицы
    print(f"{'':<12}", end="")
    for name in shape_names:
        print(f"{name:<12}", end="")
    print()
    
    # Печатаем результаты сравнения
    for i, shape1 in enumerate(shapes):
        print(f"{shape_names[i]:<12}", end="")
        for j, shape2 in enumerate(shapes):
            if i == j:
                print(f"{'—':<12}", end="")
            elif shape1.area_larger_than(shape2):
                print(f"{'больше':<12}", end="")
            else:
                print(f"{'меньше':<12}", end="")
        print()
    print()


def interactive_shape_creator():
    print("Интерактивный создатель фигур")
    print("=" * 60)
    
    while True:
        print("\nВыберите тип создаваемой фигуры:")
        print("1. Квадрат")
        print("2. Прямоугольник")
        print("3. Треугольник")
        print("4. Круг")
        print("5. Выход")
        
        choice = input("Введите выбор (1-5): ").strip()
        
        if choice == '5':
            print("Выход из создателя фигур")
            break
        
        try:
            if choice == '1':
                side = float(input("Введите длину стороны квадрата: "))
                shape = Square(side)
                print(f"Успешно создано: {shape}")
                
            elif choice == '2':
                length = float(input("Введите длину прямоугольника: "))
                width = float(input("Введите ширину прямоугольника: "))
                shape = Rectangle(length, width)
                print(f"Успешно создано: {shape}")
                
            elif choice == '3':
                a = float(input("Введите первую сторону треугольника: "))
                b = float(input("Введите вторую сторону треугольника: "))
                c = float(input("Введите третью сторону треугольника: "))
                shape = Triangle(a, b, c)
                print(f"Успешно создано: {shape}")
                
                # Отображаем тип треугольника
                if shape.is_equilateral():
                    print("  → Это равносторонний треугольник")
                elif shape.is_isosceles():
                    print("  → Это равнобедренный треугольник")
                if shape.is_right_triangle():
                    print("  → Это прямоугольный треугольник")
                    
            elif choice == '4':
                radius = float(input("Введите радиус круга: "))
                shape = Circle(radius)
                print(f"Успешно создано: {shape}")
                
            else:
                print("Неверный выбор, попробуйте снова")
                continue
            
            # Сравнение с другими фигурами (создаем несколько предустановленных фигур для сравнения)
            preset_shapes = [Square(3), Rectangle(2, 4), Triangle(3, 4, 5), Circle(2)]
            print("\nСравнение с другими фигурами:")
            for preset in preset_shapes:
                if shape.area_larger_than(preset):
                    print(f"  Площадь {shape.__class__.__name__} > Площадь {preset.__class__.__name__}")
                else:
                    print(f"  Площадь {shape.__class__.__name__} < Площадь {preset.__class__.__name__}")
                    
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Ошибка при создании фигуры: {e}")


def test_edge_cases():
    print("\nТестирование граничных случаев:")
    print("-" * 40)
    
    # Тестируем неверные входные данные
    test_cases = [
        ("Длина стороны квадрата=0", lambda: Square(0)),
        ("Длина прямоугольника=0", lambda: Rectangle(0, 5)),
        ("Неверные длины сторон треугольника", lambda: Triangle(1, 2, 5)),
        ("Радиус круга=-1", lambda: Circle(-1)),
    ]
    
    for description, test_func in test_cases:
        try:
            test_func()
            print(f"✗ {description}: должно было вызвать исключение, но не вызвало")
        except (ValueError, Exception) as e:
            print(f"✓ {description}: правильно вызвало исключение - {e}")


if __name__ == "__main__":
    
    # Демонстрация базовой функциональности
    demonstrate_shapes()
    
    # Отображение матрицы сравнения площадей
    area_comparison_matrix()
    
    # Интерактивное создание фигур
    interactive_shape_creator()
    
    # Тестирование граничных случаев
    test_edge_cases()
    
    print("\n" + "=" * 60)
    print("Задача 3 завершена! Демонстрация иерархии классов фигур окончена.")