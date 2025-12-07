"""
定义具体的lambda过滤器函数
"""

# 1. 排除字符串中的空格
exclude_spaces = lambda s: ' ' not in s

# 2. 排除以字母"а"或"a"开头的字符串（注意：俄语а和英语a）
#    这里我们处理大小写和两种语言的a
exclude_starts_with_a = lambda s: not s.lower().startswith(('a', 'а'))

# 3. 排除长度小于5的字符串
exclude_short_strings = lambda s: len(s) >= 5

# 4. 自定义的额外过滤器示例
exclude_digits = lambda s: not any(char.isdigit() for char in s)  # 排除包含数字的字符串

exclude_special_chars = lambda s: s.isalnum()  # 排除包含特殊字符的字符串

# 复合过滤器示例：同时满足多个条件
long_strings_without_spaces = lambda s: len(s) >= 5 and ' ' not in s