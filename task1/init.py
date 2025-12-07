def is_palindrome(s: str) -> bool:
    """
    检查字符串是否为回文
    
    Args:
        s (str): 要检查的字符串
        
    Returns:
        bool: 如果是回文返回True，否则返回False
    """
    # 移除空格并转换为小写以进行更通用的检查
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # 检查是否回文
    return cleaned == cleaned[::-1]


def is_palindrome_exact(s: str) -> bool:
    """
    严格检查字符串是否为回文（包括空格和大小写）
    
    Args:
        s (str): 要检查的字符串
        
    Returns:
        bool: 如果是回文返回True，否则返回False
    """
    return s == s[::-1]