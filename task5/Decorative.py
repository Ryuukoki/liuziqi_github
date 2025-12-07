import time
import functools
from typing import Any, Callable
import os


def timing_decorator(verbose: bool = True):
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Записываем время начала
            start_time = time.perf_counter()
            
            # Выполняем декорируемую функцию
            result = func(*args, **kwargs)
            
            # Записываем время окончания
            end_time = time.perf_counter()
            
            # Вычисляем время выполнения (миллисекунды)
            execution_time = (end_time - start_time) * 1000
            
            if verbose:
                print(f"Функция '{func.__name__}' выполнилась за: {execution_time:.4f} мс")
                if args:
                    print(f"   Аргументы: {args}")
                if kwargs:
                    print(f"   Именованные аргументы: {kwargs}")
                if result is not None:
                    print(f"   Возвращаемое значение: {result}")
                print("-" * 50)
            
            return result
        return wrapper
    return decorator


class PerformanceMonitor:
    
    def __init__(self, description: str = "операция"):
        self.description = description
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        print(f"Начало {self.description}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Заканчивает отсчет времени при выходе из контекстного менеджера"""
        self.end_time = time.perf_counter()
        execution_time = (self.end_time - self.start_time) * 1000
        print(f"{self.description} завершена, время: {execution_time:.4f} мс")
        print()


# ============================================================================
# Тестовая функция 1: Вычисление суммы двух чисел с выводом в консоль
# ============================================================================

@timing_decorator()
def calculate_sum(a: float, b: float) -> float:
    
    result = a + b
    print(f"Вычисление: {a} + {b} = {result}")
    return result


# ============================================================================
# Тестовая функция 2: Операции чтения и записи файлов
# ============================================================================

@timing_decorator()
def read_numbers_from_file(filename: str = "input.txt") -> tuple:
    
    print(f"Чтение файла: {filename}")
    
    # Проверяем существование файла
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не существует")
        return None, None
    
    # Проверяем, не пустой ли файл
    if os.path.getsize(filename) == 0:
        print(f"Ошибка: файл '{filename}' пуст")
        return None, None
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Прочитано {len(lines)} строк")
            
            # Показываем содержимое файла для отладки
            for i, line in enumerate(lines):
                print(f"   Строка {i+1}: '{line.strip()}'")
            
            # Фильтруем пустые строки и строки не с числами
            numbers = []
            for line in lines:
                stripped_line = line.strip()
                if stripped_line:  # непустая строка
                    try:
                        num = float(stripped_line)
                        numbers.append(num)
                        print(f"Успешно распознано число: {num}")
                    except ValueError:
                        print(f"Пропуск строки не с числом: '{stripped_line}'")
            
            if len(numbers) < 2:
                print(f"Ошибка: требуется 2 числа, но найдено только {len(numbers)} действительных чисел")
                return None, None
            
            a, b = numbers[0], numbers[1]
            print(f"Успешно прочитаны числа: {a} и {b}")
            return a, b
            
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None


@timing_decorator()
def write_result_to_file(result: float, filename: str = "output.txt"):
    
    print(f"Запись результата в файл: {filename}")
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Результат вычисления: {result}\n")
            file.write(f"Время вычисления: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Программа: Задача 5 - Демонстрация декоратора\n")
        
        print(f"Результат успешно записан в файл '{filename}'")
        return True
        
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")
        return False


@timing_decorator()
def file_based_calculation(input_file: str = "input.txt", output_file: str = "output.txt"):
    
    print("🔄 Начало процесса работы с файлами")
    
    # Шаг 1: Чтение входного файла
    with PerformanceMonitor("Чтение входного файла"):
        a, b = read_numbers_from_file(input_file)
    
    if a is None or b is None:
        print("Процесс работы с файлами прерван из-за ошибки чтения")
        return None
    
    # Шаг 2: Выполнение вычисления
    with PerformanceMonitor("Выполнение вычисления"):
        result = calculate_sum(a, b)
    
    # Шаг 3: Запись в выходной файл
    with PerformanceMonitor("Запись в выходной файл"):
        write_result_to_file(result, output_file)
    
    print("Процесс работы с файлами завершен!")
    return result


# ============================================================================
# Демонстрационные и тестовые функции
# ============================================================================

def demonstrate_basic_timing():
    """Демонстрирует базовые функции тайминга"""
    print("1. Демонстрация базовых функций тайминга")
    print("=" * 50)
    
    # Тест быстрого вычисления
    calculate_sum(5, 3)
    
    # Тест медленного вычисления (имитация)
    @timing_decorator()
    def slow_calculation():
        print("Выполняется сложное вычисление...")
        time.sleep(0.5)  # Имитация времени вычисления
        result = sum(i ** 2 for i in range(10000))
        print(f"Результат сложного вычисления: {result}")
        return result
    
    slow_calculation()


def demonstrate_file_operations():
    """Демонстрирует функции работы с файлами"""
    print("2. Демонстрация функций работы с файлами")
    print("=" * 50)
    
    # Показываем состояние текущей директории
    print("Файлы в текущей директории:")
    for file in os.listdir('.'):
        if file.endswith(('.py', '.txt')):
            size = os.path.getsize(file)
            print(f"   {file} ({size} байт)")
    
    print()
    
    # Выполняем процесс работы с файлами
    result = file_based_calculation("input.txt", "output.txt")
    
    if result is not None:
        print(f"Итоговый результат вычисления: {result}")
    else:
        print("Ошибка при работе с файлами")


def interactive_demo():
    """Интерактивная демонстрация"""
    print("3. Интерактивная демонстрация")
    print("=" * 50)
    
    while True:
        print("\nВыберите функцию для тестирования:")
        print("1. Простое вычисление с числами")
        print("2. Тест работы с файлами")
        print("3. Выход")
        
        choice = input("Введите выбор (1-3): ").strip()
        
        if choice == '1':
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                calculate_sum(a, b)
            except ValueError:
                print("Пожалуйста, введите действительные числа")
                
        elif choice == '2':
            input_file = input("Введите имя входного файла (Enter для input.txt): ").strip()
            output_file = input("Введите имя выходного файла (Enter для output.txt): ").strip()
            
            if not input_file:
                input_file = "input.txt"
            if not output_file:
                output_file = "output.txt"
            
            file_based_calculation(input_file, output_file)
            
        elif choice == '3':
            print("Выход из интерактивной демонстрации")
            break
            
        else:
            print("Неверный выбор, попробуйте снова")


def main():
    """Главная функция"""
    print("Задача 5: Декоратор для измерения времени выполнения функций")
    print("=" * 60)
    print("Автор: Ryuukoki")
    print("GitHub: liuziqi_github")
    print()
    
    # Проверяем необходимые файлы
    if not os.path.exists("input.txt"):
        print("Предупреждение: файл input.txt не существует")
        print("Создание примера файла input.txt...")
        with open("input.txt", 'w') as f:
            f.write("15.5\n23.7\n")
        print("Файл input.txt создан")
    
    # Выполняем демонстрацию
    demonstrate_basic_timing()
    print()
    demonstrate_file_operations()
    print()
    interactive_demo()
    
    print("\n" + "=" * 60)
    print("Задача 5 завершена! Спасибо за использование декоратора измерения времени выполнения.")


if __name__ == "__main__":
    main()