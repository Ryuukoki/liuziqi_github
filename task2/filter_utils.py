"""
字符串过滤工具模块
包含通用的字符串过滤函数
"""

from typing import List, Callable, Any

def filter_strings(filter_func: Callable[[str], bool], strings: List[str]) -> List[str]:
    """
    使用提供的lambda函数过滤字符串数组
    
    Args:
        filter_func: 过滤函数，接受字符串返回布尔值
        strings: 要过滤的字符串列表
        
    Returns:
        List[str]: 过滤后的字符串列表
    """
    if not callable(filter_func):
        raise TypeError("filter_func必须是一个可调用函数")
    
    if not isinstance(strings, list):
        raise TypeError("strings必须是一个列表")
    
    return [s for s in strings if filter_func(s)]


def apply_filters(filters: List[Callable[[str], bool]], strings: List[str]) -> dict:
    """
    应用多个过滤器并返回每个过滤器的结果
    
    Args:
        filters: 过滤器函数列表
        strings: 要过滤的字符串列表
        
    Returns:
        dict: 键为过滤器描述，值为过滤结果
    """
    results = {}
    for filter_func in filters:
        # 使用函数名作为键，如果没有名字则使用字符串表示
        key = filter_func.__name__ if hasattr(filter_func, '__name__') else str(filter_func)
        results[key] = filter_strings(filter_func, strings)
    
    return results