"""
过滤函数的单元测试
"""

import unittest
from filter_utils import filter_strings
from lambda_filters import exclude_spaces, exclude_starts_with_a, exclude_short_strings


class TestFilterFunctions(unittest.TestCase):
    
    def setUp(self):
        self.test_strings = [
            "apple",
            "banana split",
            "апельсин",  # 以俄语а开头
            "orange",
            "kiwi",
            "strawberry pie",
            "grape123",
            "watermelon",
            "a peach",
            "pineapple"
        ]
    
    def test_exclude_spaces(self):
        """测试排除空格"""
        result = filter_strings(exclude_spaces, self.test_strings)
        # 检查结果中是否包含空格
        for s in result:
            self.assertNotIn(' ', s)
        
        # 具体验证
        self.assertIn("apple", result)
        self.assertNotIn("banana split", result)
    
    def test_exclude_starts_with_a(self):
        """测试排除以a/а开头的字符串"""
        result = filter_strings(exclude_starts_with_a, self.test_strings)
        
        # 检查结果不以a或а开头
        for s in result:
            self.assertFalse(s.lower().startswith(('a', 'а')))
        
        self.assertNotIn("apple", result)
        self.assertNotIn("апельсин", result)
        self.assertIn("banana split", result)
    
    def test_exclude_short_strings(self):
        """测试排除短字符串"""
        result = filter_strings(exclude_short_strings, self.test_strings)
        
        # 检查所有结果长度>=5
        for s in result:
            self.assertGreaterEqual(len(s), 5)
        
        self.assertIn("apple", result)
        self.assertNotIn("kiwi", result)  # kiwi长度=4
    
    def test_empty_list(self):
        """测试空列表"""
        result = filter_strings(exclude_spaces, [])
        self.assertEqual(result, [])
    
    def test_custom_lambda(self):
        """测试自定义lambda函数"""
        # 自定义lambda：只保留包含字母'a'的字符串
        contains_a = lambda s: 'a' in s.lower()
        result = filter_strings(contains_a, self.test_strings)
        
        for s in result:
            self.assertIn('a', s.lower())
    
    def test_invalid_inputs(self):
        """测试无效输入"""
        with self.assertRaises(TypeError):
            filter_strings("not a function", self.test_strings)
        
        with self.assertRaises(TypeError):
            filter_strings(exclude_spaces, "not a list")


def run_tests():
    """运行测试"""
    print("运行过滤器测试...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilterFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n所有测试通过!")
    else:
        print(f"\n测试失败: {len(result.failures)}个失败")


if __name__ == "__main__":
    run_tests()