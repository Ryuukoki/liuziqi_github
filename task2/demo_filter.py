"""
演示如何使用过滤函数
"""

from filter_utils import filter_strings, apply_filters
from lambda_filters import (
    exclude_spaces, 
    exclude_starts_with_a, 
    exclude_short_strings,
    exclude_digits,
    long_strings_without_spaces
)


def demonstrate_basic_filters():
    """演示基本过滤器"""
    # 测试数据
    test_strings = [
        "apple",
        "banana split",
        "апельсин",  # 俄语"橙子"，以а开头
        "orange",
        "kiwi",
        "strawberry pie",
        "grape123",
        "watermelon",
        "a peach",
        "pineapple"
    ]
    
    print("原始字符串列表:")
    for i, s in enumerate(test_strings, 1):
        print(f"{i}. '{s}'")
    
    print("\n" + "=" * 50 + "\n")
    
    # 1. 排除字符串中的空格
    filtered_no_spaces = filter_strings(exclude_spaces, test_strings)
    print("1. 排除包含空格的字符串:")
    print(f"   结果: {filtered_no_spaces}")
    print(f"   剩余数量: {len(filtered_no_spaces)}\n")
    
    # 2. 排除以字母"а"/"a"开头的字符串
    filtered_no_a_start = filter_strings(exclude_starts_with_a, test_strings)
    print("2. 排除以字母'а'或'a'开头的字符串:")
    print(f"   结果: {filtered_no_a_start}")
    print(f"   剩余数量: {len(filtered_no_a_start)}\n")
    
    # 3. 排除长度小于5的字符串
    filtered_long_strings = filter_strings(exclude_short_strings, test_strings)
    print("3. 排除长度小于5的字符串:")
    print(f"   结果: {filtered_long_strings}")
    print(f"   剩余数量: {len(filtered_long_strings)}\n")
    
    # 4. 使用复合过滤器
    filtered_complex = filter_strings(long_strings_without_spaces, test_strings)
    print("4. 复合过滤器(长度≥5且无空格):")
    print(f"   结果: {filtered_complex}")
    print(f"   剩余数量: {len(filtered_complex)}\n")
    
    return test_strings


def demonstrate_apply_filters():
    """演示apply_filters函数"""
    test_strings = ["hello", "world wide", "apple", "an orange", "test", "12345"]
    
    print("演示apply_filters函数:")
    print(f"测试数据: {test_strings}\n")
    
    # 定义过滤器列表
    filters = [
        exclude_spaces,
        exclude_starts_with_a,
        exclude_short_strings,
        exclude_digits,
        lambda s: 'e' in s  # 内联lambda：包含字母e
    ]
    
    # 应用所有过滤器
    results = apply_filters(filters, test_strings)
    
    for filter_name, filtered in results.items():
        print(f"过滤器 '{filter_name}': {filtered}")


def interactive_demo():
    """交互式演示"""
    print("交互式过滤器演示")
    print("=" * 50)
    
    # 让用户输入字符串
    user_input = input("请输入多个字符串，用逗号分隔: ")
    strings = [s.strip() for s in user_input.split(',')]
    
    print(f"\n您输入的字符串: {strings}")
    
    # 选择过滤器
    print("\n请选择过滤器:")
    print("1. 排除包含空格的字符串")
    print("2. 排除以'a'或'а'开头的字符串")
    print("3. 排除长度小于5的字符串")
    print("4. 自定义lambda表达式")
    
    choice = input("\n请输入选择(1-4): ")
    
    if choice == '1':
        filtered = filter_strings(exclude_spaces, strings)
        print(f"\n结果: {filtered}")
    elif choice == '2':
        filtered = filter_strings(exclude_starts_with_a, strings)
        print(f"\n结果: {filtered}")
    elif choice == '3':
        filtered = filter_strings(exclude_short_strings, strings)
        print(f"\n结果: {filtered}")
    elif choice == '4':
        lambda_expr = input("请输入lambda表达式(如: lambda s: 'a' in s): ")
        try:
            # 注意：使用eval有安全风险，仅用于演示
            filter_func = eval(lambda_expr)
            filtered = filter_strings(filter_func, strings)
            print(f"\n结果: {filtered}")
        except Exception as e:
            print(f"错误: {e}")
    else:
        print("无效选择")


def main():
    """主函数"""
    print("字符串过滤器演示程序")
    print("=" * 50)
    
    while True:
        print("\n请选择演示模式:")
        print("1. 基本过滤器演示")
        print("2. 多过滤器应用演示")
        print("3. 交互式演示")
        print("4. 退出")
        
        choice = input("\n请输入选择(1-4): ")
        
        if choice == '1':
            demonstrate_basic_filters()
        elif choice == '2':
            demonstrate_apply_filters()
        elif choice == '3':
            interactive_demo()
        elif choice == '4':
            print("再见!")
            break
        else:
            print("无效选择，请重试")


if __name__ == "__main__":
    main()