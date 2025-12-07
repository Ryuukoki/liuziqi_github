from main import is_palindrome, is_palindrome_exact


def test_palindrome():
    """测试回文检查功能"""
    
    # 测试用例
    test_cases = [
        ("racecar", True),           # 简单回文
        ("A man a plan a canal Panama", True),  # 带空格的回文
        ("hello", False),            # 不是回文
        ("", True),                  # 空字符串
        ("a", True),                 # 单字符
        ("12321", True),             # 数字回文
        ("Was it a car or a cat I saw?", True),  # 带标点的回文
        ("not a palindrome", False)  # 不是回文
    ]
    
    print("测试 is_palindrome (通用检查):")
    for test_string, expected in test_cases:
        result = is_palindrome(test_string)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{test_string[:20]}...' -> {result} (预期: {expected})")
    
    print("\n测试 is_palindrome_exact (严格检查):")
    strict_cases = [
        ("racecar", True),
        ("Racecar", False),  # 严格检查会认为这个不是回文
        ("ab ba", True),
        ("ab ba ", False)    # 严格检查空格
    ]
    
    for test_string, expected in strict_cases:
        result = is_palindrome_exact(test_string)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{test_string}' -> {result} (预期: {expected})")


def main():
    """主函数：演示回文检查"""
    print("回文检查演示")
    print("=" * 50)
    
    # 用户输入演示
    user_input = input("请输入要检查的字符串: ")
    
    if is_palindrome(user_input):
        print(f"✓ '{user_input}' 是回文")
    else:
        print(f"✗ '{user_input}' 不是回文")
    
    print("\n" + "=" * 50)
    print("自动测试结果:")
    test_palindrome()


if __name__ == "__main__":
    main()