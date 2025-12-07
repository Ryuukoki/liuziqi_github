"""
任务4包初始化文件
"""
from .university import Person, Student, Aspirant
from .financial import (
    calculate_student_scholarship,
    calculate_aspirant_scholarship,
    compare_scholarships,
    get_scholarship_stats
)

__all__ = [
    'Person',
    'Student',
    'Aspirant',
    'calculate_student_scholarship',
    'calculate_aspirant_scholarship',
    'compare_scholarships',
    'get_scholarship_stats'
]