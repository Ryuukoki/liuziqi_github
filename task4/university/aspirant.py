"""
研究生类，继承自Student
"""
from university.student import Student
from financial.scholarship import calculate_aspirant_scholarship


class Aspirant(Student):
    """研究生类，继承自Student"""
    
    def __init__(self, first_name: str, last_name: str, age: int, 
                 group_number: str, average_score: float, 
                 research_work: str):
        """
        初始化研究生
        
        Args:
            first_name: 名
            last_name: 姓
            age: 年龄
            group_number: 组号/学号
            average_score: 平均分（0-5）
            research_work: 科研工作/论文题目
        """
        super().__init__(first_name, last_name, age, group_number, average_score)
        self.research_work = research_work
    
    def get_info(self) -> str:
        """获取研究生信息（扩展父类方法）"""
        base_info = super().get_info()
        return f"{base_info}, 科研工作: {self.research_work}"
    
    def get_scholarship(self) -> float:
        """获取研究生奖学金金额"""
        return calculate_aspirant_scholarship(self.average_score)
    
    def compare_scholarship(self, other: 'Student') -> dict:
        """与另一个学生/研究生比较奖学金
        
        Args:
            other: 可以是Student或Aspirant对象
            
        Returns:
            dict: 包含比较结果的字典
        """
        my_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()
        
        other_type = "研究生" if isinstance(other, Aspirant) else "学生"
        
        return {
            '当前研究生': self.get_full_name(),
            f'另一{other_type}': other.get_full_name(),
            '当前奖学金': my_scholarship,
            '另一奖学金': other_scholarship,
            '比较结果': {
                '当前更多': my_scholarship > other_scholarship,
                '当前更少': my_scholarship < other_scholarship,
                '相等': my_scholarship == other_scholarship
            }
        }
    
    def get_research_info(self) -> str:
        """获取科研工作信息"""
        return f"科研课题: {self.research_work}"
    
    def __repr__(self) -> str:
        return (f"Aspirant(first_name='{self.first_name}', last_name='{self.last_name}', "
                f"age={self.age}, group_number='{self.group_number}', "
                f"average_score={self.average_score}, research_work='{self.research_work}')")
    
    def to_dict(self) -> dict:
        """将研究生信息转换为字典"""
        return {
            'type': 'aspirant',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'group_number': self.group_number,
            'average_score': self.average_score,
            'research_work': self.research_work,
            'scholarship': self.get_scholarship()
        }