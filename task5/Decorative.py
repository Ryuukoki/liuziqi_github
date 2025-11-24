"""
任务5：函数执行时间测量装饰器
主程序文件 - Decorative.py
"""

import time
import functools
from typing import Any, Callable
import os


def timing_decorator(verbose: bool = True):
    """
    测量函数执行时间的装饰器
    
    参数:
    verbose: 是否在控制台输出执行时间信息
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # 记录开始时间
            start_time = time.perf_counter()
            
            # 执行被装饰的函数
            result = func(*args, **kwargs)
            
            # 记录结束时间
            end_time = time.perf_counter()
            
            # 计算执行时间（毫秒）
            execution_time = (end_time - start_time) * 1000
            
            if verbose:
                print(f"⏱️  函数 '{func.__name__}' 执行耗时: {execution_time:.4f} 毫秒")
                if args:
                    print(f"   参数: {args}")
                if kwargs:
                    print(f"   关键字参数: {kwargs}")
                if result is not None:
                    print(f"   返回值: {result}")
                print("-" * 50)
            
            return result
        return wrapper
    return decorator


class PerformanceMonitor:
    """
    性能监控器类，提供更高级的计时功能
    """
    
    def __init__(self, description: str = "操作"):
        self.description = description
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        """进入上下文管理器时开始计时"""
        self.start_time = time.perf_counter()
        print(f"🚀 开始 {self.description}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器时结束计时"""
        self.end_time = time.perf_counter()
        execution_time = (self.end_time - self.start_time) * 1000
        print(f"✅ {self.description}完成，耗时: {execution_time:.4f} 毫秒")
        print()


# ============================================================================
# 测试函数1：计算两个数字的和并在控制台输出
# ============================================================================

@timing_decorator()
def calculate_sum(a: float, b: float) -> float:
    """
    计算两个数字的和并在控制台输出结果
    
    参数:
    a: 第一个数字
    b: 第二个数字
    
    返回:
    float: 两个数字的和
    """
    result = a + b
    print(f"📊 计算: {a} + {b} = {result}")
    return result


# ============================================================================
# 测试函数2：文件读写操作
# ============================================================================

@timing_decorator()
def read_numbers_from_file(filename: str = "input.txt") -> tuple:
    """
    从文件读取两个数字
    
    参数:
    filename: 输入文件名
    
    返回:
    tuple: 包含两个数字的元组，如果出错返回 (None, None)
    """
    print(f"📖 正在读取文件: {filename}")
    
    # 检查文件是否存在
    if not os.path.exists(filename):
        print(f"❌ 错误: 文件 '{filename}' 不存在")
        return None, None
    
    # 检查文件是否为空
    if os.path.getsize(filename) == 0:
        print(f"❌ 错误: 文件 '{filename}' 为空")
        return None, None
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"📄 读取到 {len(lines)} 行内容")
            
            # 显示文件内容用于调试
            for i, line in enumerate(lines):
                print(f"   第{i+1}行: '{line.strip()}'")
            
            # 过滤空行和非数字行
            numbers = []
            for line in lines:
                stripped_line = line.strip()
                if stripped_line:  # 非空行
                    try:
                        num = float(stripped_line)
                        numbers.append(num)
                        print(f"✅ 成功解析数字: {num}")
                    except ValueError:
                        print(f"⚠️  跳过非数字行: '{stripped_line}'")
            
            if len(numbers) < 2:
                print(f"❌ 错误: 需要2个数字，但只找到 {len(numbers)} 个有效数字")
                return None, None
            
            a, b = numbers[0], numbers[1]
            print(f"✅ 成功读取数字: {a} 和 {b}")
            return a, b
            
    except Exception as e:
        print(f"❌ 读取文件时出错: {e}")
        return None, None


@timing_decorator()
def write_result_to_file(result: float, filename: str = "output.txt"):
    """
    将结果写入文件
    
    参数:
    result: 要写入的结果
    filename: 输出文件名
    """
    print(f"📝 正在写入结果到文件: {filename}")
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"计算结果: {result}\n")
            file.write(f"计算时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"程序: 任务5 - 装饰器演示\n")
        
        print(f"✅ 结果已成功写入文件 '{filename}'")
        return True
        
    except Exception as e:
        print(f"❌ 写入文件时出错: {e}")
        return False


@timing_decorator()
def file_based_calculation(input_file: str = "input.txt", output_file: str = "output.txt"):
    """
    完整的文件操作流程：读取文件、计算、写入结果
    
    参数:
    input_file: 输入文件名
    output_file: 输出文件名
    
    返回:
    float: 计算结果，如果出错返回 None
    """
    print("🔄 开始文件操作流程")
    
    # 步骤1：读取输入文件
    with PerformanceMonitor("读取输入文件"):
        a, b = read_numbers_from_file(input_file)
    
    if a is None or b is None:
        print("❌ 文件操作流程因读取错误而终止")
        return None
    
    # 步骤2：进行计算
    with PerformanceMonitor("执行计算"):
        result = calculate_sum(a, b)
    
    # 步骤3：写入输出文件
    with PerformanceMonitor("写入输出文件"):
        write_result_to_file(result, output_file)
    
    print("🎉 文件操作流程完成！")
    return result


# ============================================================================
# 演示和测试函数
# ============================================================================

def demonstrate_basic_timing():
    """演示基本的计时功能"""
    print("1. 基本计时功能演示")
    print("=" * 50)
    
    # 测试快速计算
    calculate_sum(5, 3)
    
    # 测试较慢的计算（模拟）
    @timing_decorator()
    def slow_calculation():
        print("正在进行复杂计算...")
        time.sleep(0.5)  # 模拟计算耗时
        result = sum(i ** 2 for i in range(10000))
        print(f"复杂计算结果: {result}")
        return result
    
    slow_calculation()


def demonstrate_file_operations():
    """演示文件操作功能"""
    print("2. 文件操作功能演示")
    print("=" * 50)
    
    # 显示当前目录状态
    print("📁 当前目录文件:")
    for file in os.listdir('.'):
        if file.endswith(('.py', '.txt')):
            size = os.path.getsize(file)
            print(f"   {file} ({size} 字节)")
    
    print()
    
    # 执行文件操作流程
    result = file_based_calculation("input.txt", "output.txt")
    
    if result is not None:
        print(f"🎯 最终计算结果: {result}")
    else:
        print("💥 文件操作失败")


def interactive_demo():
    """交互式演示"""
    print("3. 交互式演示")
    print("=" * 50)
    
    while True:
        print("\n选择要测试的功能:")
        print("1. 简单数字计算")
        print("2. 文件操作测试")
        print("3. 退出")
        
        choice = input("请输入选择 (1-3): ").strip()
        
        if choice == '1':
            try:
                a = float(input("请输入第一个数字: "))
                b = float(input("请输入第二个数字: "))
                calculate_sum(a, b)
            except ValueError:
                print("❌ 请输入有效的数字")
                
        elif choice == '2':
            input_file = input("请输入输入文件名 (回车使用 input.txt): ").strip()
            output_file = input("请输入输出文件名 (回车使用 output.txt): ").strip()
            
            if not input_file:
                input_file = "input.txt"
            if not output_file:
                output_file = "output.txt"
            
            file_based_calculation(input_file, output_file)
            
        elif choice == '3':
            print("👋 退出交互式演示")
            break
            
        else:
            print("❌ 无效选择，请重新输入")


def main():
    """主函数"""
    print("任务5：函数执行时间测量装饰器")
    print("=" * 60)
    print("作者: Ryuukoki")
    print("GitHub: liuziqi_github")
    print()
    
    # 检查必要文件
    if not os.path.exists("input.txt"):
        print("⚠️  警告: input.txt 文件不存在")
        print("正在创建示例 input.txt 文件...")
        with open("input.txt", 'w') as f:
            f.write("15.5\n23.7\n")
        print("✅ 已创建 input.txt 文件")
    
    # 执行演示
    demonstrate_basic_timing()
    print()
    demonstrate_file_operations()
    print()
    interactive_demo()
    
    print("\n" + "=" * 60)
    print("任务5完成！感谢使用函数执行时间测量装饰器。")


if __name__ == "__main__":
    main()