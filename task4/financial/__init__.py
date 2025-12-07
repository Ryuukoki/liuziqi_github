"""
金融模块初始化文件
"""
from .scholarship import (
    calculate_student_scholarship,
    calculate_aspirant_scholarship,
    compare_scholarships,
    get_scholarship_stats
)

__all__ = [
    'calculate_student_scholarship',
    'calculate_aspirant_scholarship',
    'compare_scholarships',
    'get_scholarship_stats'
]