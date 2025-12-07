"""
学生和研究生类演示程序
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from university import Student, Aspirant
from financial import get_scholarship_stats


def create_sample_students():
    """创建示例学生和研究生"""
    print("=" * 60)
    print("创建示例学生和研究生")
    print("=" * 60)
    
    # 创建学生
    student1 = Student("伊万", "伊万诺夫", 20, "ГР-101", 4.8)
    student2 = Student("玛丽亚", "彼得罗娃", 21, "ГР-102", 5.0)
    student3 = Student("亚历山大", "西多罗夫", 19, "ГР-101", 4.5)
    
    # 创建研究生
    aspirant1 = Aspirant("谢尔盖", "斯米尔诺夫", 25, "АСП-201", 4.9, 
                        "人工智能在医疗诊断中的应用")
    aspirant2 = Aspirant("奥莉加", "瓦西里耶娃", 26, "АСП-202", 5.0, 
                        "量子计算算法研究")
    aspirant3 = Aspirant("阿列克谢", "费奥多罗夫", 24, "АСП-201", 4.7, 
                        "区块链技术安全优化")
    
    all_persons = [student1, student2, student3, aspirant1, aspirant2, aspirant3]
    
    # 显示所有人员信息
    for person in all_persons:
        print()
        person.display_info()
        person.display_scholarship()
    
    return student1, student2, student3, aspirant1, aspirant2, aspirant3


def demonstrate_scholarship_calculations():
    """演示奖学金计算"""
    print("\n" + "=" * 60)
    print("奖学金计算演示")
    print("=" * 60)
    
    # 测试不同平均分的学生
    test_students = [
        ("学生A", "组1", 5.0),
        ("学生B", "组1", 4.9),
        ("学生C", "组2", 3.0),
        ("学生D", "组2", 2.5)
    ]
    
    print("\n学生奖学金计算:")
    for name, group, score in test_students:
        student = Student(name, "测试", 20, group, score)
        scholarship = student.get_scholarship()
        print(f"  {name} (平均分{score}): {scholarship:.0f}₽")
    
    # 测试不同平均分的研究生
    print("\n研究生奖学金计算:")
    test_aspirants = [
        ("研究生A", "АСП-1", 5.0, "研究课题A"),
        ("研究生B", "АСП-1", 4.8, "研究课题B"),
        ("研究生C", "АСП-2", 3.5, "研究课题C"),
        ("研究生D", "АСП-2", 2.0, "研究课题D")
    ]
    
    for name, group, score, research in test_aspirants:
        aspirant = Aspirant(name, "测试", 25, group, score, research)
        scholarship = aspirant.get_scholarship()
        print(f"  {name} (平均分{score}): {scholarship:.0f}₽")


def demonstrate_comparisons():
    """演示奖学金比较"""
    print("\n" + "=" * 60)
    print("奖学金比较演示")
    print("=" * 60)
    
    # 创建测试对象
    student1 = Student("学生A", "测试", 20, "ГР-101", 5.0)  # 6000
    student2 = Student("学生B", "测试", 21, "ГР-102", 4.5)  # 4000
    aspirant1 = Aspirant("研究生A", "测试", 25, "АСП-201", 5.0, "研究1")  # 8000
    aspirant2 = Aspirant("研究生B", "测试", 26, "АСП-202", 4.5, "研究2")  # 6000
    
    print("\n1. 学生之间的比较:")
    comparison = student1.compare_scholarship(student2)
    print(f"   {comparison['当前学生']} ({comparison['当前奖学金']}₽) vs "
          f"{comparison['另一学生']} ({comparison['另一奖学金']}₽)")
    print(f"   结果: {comparison['当前学生']}的奖学金", 
          "更多" if comparison['比较结果']['当前更多'] else 
          "更少" if comparison['比较结果']['当前更少'] else "相等")
    
    print("\n2. 研究生与学生比较:")
    comparison = aspirant1.compare_scholarship(student1)
    print(f"   {comparison['当前研究生']} ({comparison['当前奖学金']}₽) vs "
          f"{comparison['另一学生']} ({comparison['另一奖学金']}₽)")
    print(f"   结果: {comparison['当前研究生']}的奖学金", 
          "更多" if comparison['比较结果']['当前更多'] else 
          "更少" if comparison['比较结果']['当前更少'] else "相等")
    
    print("\n3. 研究生之间的比较:")
    comparison = aspirant1.compare_scholarship(aspirant2)
    print(f"   {comparison['当前研究生']} ({comparison['当前奖学金']}₽) vs "
          f"{comparison['另一研究生']} ({comparison['另一奖学金']}₽)")
    print(f"   结果: {comparison['当前研究生']}的奖学金", 
          "更多" if comparison['比较结果']['当前更多'] else 
          "更少" if comparison['比较结果']['当前更少'] else "相等")


def demonstrate_statistics():
    """演示统计功能"""
    print("\n" + "=" * 60)
    print("统计功能演示")
    print("=" * 60)
    
    # 创建一组学生和研究生
    persons = [
        Student("学生1", "测试", 20, "ГР-101", 5.0),
        Student("学生2", "测试", 21, "ГР-101", 4.2),
        Student("学生3", "测试", 22, "ГР-102", 3.8),
        Student("学生4", "测试", 20, "ГР-103", 4.9),
        Aspirant("研究生1", "测试", 25, "АСП-201", 5.0, "研究A"),
        Aspirant("研究生2", "测试", 26, "АСП-202", 4.5, "研究B"),
        Aspirant("研究生3", "测试", 24, "АСП-201", 4.7, "研究C"),
        Aspirant("研究生4", "测试", 27, "АСП-203", 3.5, "研究D")
    ]
    
    stats = get_scholarship_stats(persons)
    
    print("\n奖学金统计:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value}")
    
    # 显示详细信息
    print("\n详细信息:")
    total_scholarship = 0
    for person in persons:
        scholarship = person.get_scholarship()
        total_scholarship += scholarship
        person_type = "研究生" if isinstance(person, Aspirant) else "学生"
        print(f"  {person.get_full_name()} ({person_type}): {scholarship:.0f}₽")
    
    print(f"\n  总计: {total_scholarship:.0f}₽")


def load_from_files():
    """从文件加载学生和研究生数据"""
    print("\n" + "=" * 60)
    print("从文件加载数据")
    print("=" * 60)
    
    persons = []
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    # 加载学生数据
    students_file = os.path.join(data_dir, "students.txt")
    if os.path.exists(students_file):
        with open(students_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        parts = line.split(',')
                        if len(parts) == 5:
                            first_name, last_name, age_str, group, score_str = parts
                            student = Student(first_name.strip(), last_name.strip(), 
                                            int(age_str.strip()), group.strip(), 
                                            float(score_str.strip()))
                            persons.append(student)
                    except Exception as e:
                        print(f"警告: 第{line_num}行解析失败: {line} ({e})")
    
    # 加载研究生数据
    aspirants_file = os.path.join(data_dir, "aspirants.txt")
    if os.path.exists(aspirants_file):
        with open(aspirants_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        parts = line.split(',', 5)  # 最多分割5次
                        if len(parts) == 6:
                            first_name, last_name, age_str, group, score_str, research = parts
                            aspirant = Aspirant(first_name.strip(), last_name.strip(), 
                                              int(age_str.strip()), group.strip(), 
                                              float(score_str.strip()), research.strip())
                            persons.append(aspirant)
                    except Exception as e:
                        print(f"警告: 第{line_num}行解析失败: {line} ({e})")
    
    # 显示加载的数据
    if persons:
        print(f"\n成功加载 {len(persons)} 名学生/研究生:")
        for person in persons:
            person_type = "研究生" if isinstance(person, Aspirant) else "学生"
            print(f"  {person.get_full_name()} ({person_type}, {person.get_scholarship()}₽)")
        
        # 显示统计
        stats = get_scholarship_stats(persons)
        print(f"\n统计:")
        print(f"  总人数: {stats['总人数']}")
        print(f"  学生人数: {stats['学生人数']}")
        print(f"  研究生人数: {stats['研究生人数']}")
        print(f"  奖学金总额: {stats['奖学金总额']:.0f}₽")
    else:
        print("没有加载到数据")
    
    return persons


def interactive_demo():
    """交互式演示"""
    print("\n" + "=" * 60)
    print("交互式演示")
    print("=" * 60)
    
    persons = []
    
    while True:
        print("\n请选择操作:")
        print("1. 添加学生")
        print("2. 添加研究生")
        print("3. 查看所有人员")
        print("4. 比较奖学金")
        print("5. 查看统计")
        print("6. 返回主菜单")
        
        choice = input("请输入选择 (1-6): ")
        
        if choice == '1':
            print("\n添加新学生:")
            first_name = input("名: ")
            last_name = input("姓: ")
            age = int(input("年龄: "))
            group = input("组号: ")
            score = float(input("平均分 (0-5): "))
            
            try:
                student = Student(first_name, last_name, age, group, score)
                persons.append(student)
                print(f"成功添加学生: {student.get_full_name()}")
            except ValueError as e:
                print(f"错误: {e}")
        
        elif choice == '2':
            print("\n添加新研究生:")
            first_name = input("名: ")
            last_name = input("姓: ")
            age = int(input("年龄: "))
            group = input("组号: ")
            score = float(input("平均分 (0-5): "))
            research = input("科研工作/论文题目: ")
            
            try:
                aspirant = Aspirant(first_name, last_name, age, group, score, research)
                persons.append(aspirant)
                print(f"成功添加研究生: {aspirant.get_full_name()}")
            except ValueError as e:
                print(f"错误: {e}")
        
        elif choice == '3':
            if not persons:
                print("还没有添加任何人员")
            else:
                print(f"\n当前有 {len(persons)} 名人员:")
                for i, person in enumerate(persons, 1):
                    person_type = "研究生" if isinstance(person, Aspirant) else "学生"
                    print(f"\n{i}. {person_type}: {person.get_info()}")
                    print(f"   奖学金: {person.get_scholarship()}₽")
        
        elif choice == '4':
            if len(persons) < 2:
                print("至少需要2名人员才能比较")
            else:
                print("\n选择要比较的人员:")
                for i, person in enumerate(persons, 1):
                    person_type = "研究生" if isinstance(person, Aspirant) else "学生"
                    print(f"{i}. {person.get_full_name()} ({person_type})")
                
                try:
                    idx1 = int(input("选择第一个人: ")) - 1
                    idx2 = int(input("选择第二个人: ")) - 1
                    
                    if 0 <= idx1 < len(persons) and 0 <= idx2 < len(persons):
                        person1 = persons[idx1]
                        person2 = persons[idx2]
                        
                        # 使用适当的比较方法
                        if hasattr(person1, 'compare_scholarship'):
                            comparison = person1.compare_scholarship(person2)
                            print(f"\n比较结果:")
                            print(f"  {comparison['当前研究生' if isinstance(person1, Aspirant) else '当前学生']}: "
                                  f"{comparison['当前奖学金']}₽")
                            print(f"  {comparison['另一研究生' if isinstance(person2, Aspirant) else '另一学生']}: "
                                  f"{comparison['另一奖学金']}₽")
                            
                            result = comparison['比较结果']
                            if result['当前更多']:
                                print(f"  {person1.get_full_name()} 的奖学金更多")
                            elif result['当前更少']:
                                print(f"  {person1.get_full_name()} 的奖学金更少")
                            else:
                                print(f"  两人的奖学金相等")
                    else:
                        print("无效的选择")
                except ValueError:
                    print("请输入有效的数字")
        
        elif choice == '5':
            if persons:
                stats = get_scholarship_stats(persons)
                print("\n统计信息:")
                for key, value in stats.items():
                    if isinstance(value, float):
                        print(f"  {key}: {value:.2f}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print("还没有添加任何人员")
        
        elif choice == '6':
            break
        
        else:
            print("无效选择，请重试")


def main():
    """主函数"""
    print("学生和研究生管理系统演示")
    print("=" * 60)
    
    # 创建示例数据
    sample_students = create_sample_students()
    
    while True:
        print("\n请选择演示模式:")
        print("1. 奖学金计算演示")
        print("2. 奖学金比较演示")
        print("3. 统计功能演示")
        print("4. 从文件加载数据")
        print("5. 交互式演示")
        print("6. 退出")
        
        choice = input("\n请输入选择 (1-6): ")
        
        if choice == '1':
            demonstrate_scholarship_calculations()
        elif choice == '2':
            demonstrate_comparisons()
        elif choice == '3':
            demonstrate_statistics()
        elif choice == '4':
            load_from_files()
        elif choice == '5':
            interactive_demo()
        elif choice == '6':
            print("再见!")
            break
        else:
            print("无效选择，请重试")


if __name__ == "__main__":
    main()