"""
奖学金计算模块
包含学生和研究生的奖学金计算规则
"""


def calculate_student_scholarship(average_score: float) -> float:
    """
    计算学生奖学金
    
    Args:
        average_score: 平均分（0-5）
        
    Returns:
        float: 奖学金金额（卢布）
        
    Raises:
        ValueError: 如果平均分不在0-5范围内
    """
    if not 0 <= average_score <= 5:
        raise ValueError("平均分必须在0到5之间")
    
    if average_score == 5.0:
        return 6000.0
    elif average_score < 5.0:
        return 4000.0
    else:
        return 0.0


def calculate_aspirant_scholarship(average_score: float) -> float:
    """
    计算研究生奖学金
    
    Args:
        average_score: 平均分（0-5）
        
    Returns:
        float: 奖学金金额（卢布）
        
    Raises:
        ValueError: 如果平均分不在0-5范围内
    """
    if not 0 <= average_score <= 5:
        raise ValueError("平均分必须在0到5之间")
    
    if average_score == 5.0:
        return 8000.0
    elif average_score < 5.0:
        return 6000.0
    else:
        return 0.0


def compare_scholarships(scholarship1: float, scholarship2: float) -> dict:
    """
    比较两个奖学金金额
    
    Args:
        scholarship1: 第一个奖学金金额
        scholarship2: 第二个奖学金金额
        
    Returns:
        dict: 包含比较结果的字典
    """
    return {
        '第一个金额': scholarship1,
        '第二个金额': scholarship2,
        '比较结果': {
            '第一个更多': scholarship1 > scholarship2,
            '第一个更少': scholarship1 < scholarship2,
            '相等': scholarship1 == scholarship2
        }
    }


def get_scholarship_stats(students: list) -> dict:
    """
    获取奖学金统计信息
    
    Args:
        students: 学生/研究生对象列表
        
    Returns:
        dict: 统计信息
    """
    total_scholarship = 0.0
    student_count = 0
    aspirant_count = 0
    scholarship_recipients = 0
    
    for student in students:
        scholarship = student.get_scholarship()
        total_scholarship += scholarship
        
        if scholarship > 0:
            scholarship_recipients += 1
        
        if hasattr(student, 'research_work'):
            aspirant_count += 1
        else:
            student_count += 1
    
    return {
        '总人数': len(students),
        '学生人数': student_count,
        '研究生人数': aspirant_count,
        '获得奖学金人数': scholarship_recipients,
        '奖学金总额': total_scholarship,
        '平均奖学金': total_scholarship / len(students) if students else 0
    }