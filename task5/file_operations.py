import time

# 装饰器定义
def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间: {execution_time:.6f} 秒")
        return result
    return wrapper

# 被装饰的函数
@timeit_decorator
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

@timeit_decorator
def file_operations():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        numbers = []
        for line in lines:
            line = line.strip()
            if line:
                numbers.extend(line.split())
        
        if len(numbers) < 2:
            print("错误: input.txt 中需要至少两个数字")
            return None
            
        a = float(numbers[0])
        b = float(numbers[1])
        result = a + b
        
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(f"{a} + {b} = {result}")
        
        print(f"结果已写入 output.txt: {a} + {b} = {result}")
        return result
    
    except FileNotFoundError:
        print("错误: 找不到 input.txt 文件")
        return None
    except ValueError:
        print("错误: 文件格式不正确，请确保包含有效的数字")
        return None
    except Exception as e:
        print(f"错误: {e}")
        return None

def main():
    print("=" * 50)
    print("任务5测试 - 装饰器测量函数执行时间")
    print("=" * 50)
    
    print("\n1. 测试 add_numbers 函数:")
    print("-" * 30)
    add_numbers(10, 20)
    add_numbers(123.45, 67.89)
    
    print("\n2. 测试 file_operations 函数:")
    print("-" * 30)
    file_operations()
    
    print("\n" + "=" * 50)
    print("测试完成!")
    print("=" * 50)

if __name__ == "__main__":
    main()