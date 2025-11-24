from abc import ABC, abstractmethod
from typing import Union

class Person(ABC):
    
    def __init__(self, name: str, age: int):
        
        if not name or not isinstance(name, str):
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(age, int) or age < 0 or age > 120:
            raise ValueError("Возраст должен быть целым числом от 0 до 120")
        
        self.name = name
        self.age = age
    
    def display_info(self) -> None:
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
    
    @abstractmethod
    def calculate_scholarship(self) -> float:
        pass
    
    @abstractmethod
    def scholarship_comparison(self, other) -> str:
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.age} лет)"


class Student(Person):
    
    def __init__(self, name: str, age: int, group: str, avg_grade: float):
        
        super().__init__(name, age)
        
        if not group or not isinstance(group, str):
            raise ValueError("Номер группы должен быть непустой строкой")
        if not isinstance(avg_grade, (int, float)) or avg_grade < 0 or avg_grade > 5:
            raise ValueError("Средний балл должен быть числом от 0 до 5")
        
        self.group = group
        self.avg_grade = avg_grade
    
    def display_info(self) -> None:
        super().display_info()
        print(f"Группа: {self.group}")
        print(f"Средний балл: {self.avg_grade:.2f}")
        scholarship = self.calculate_scholarship()
        print(f"Стипендия: {scholarship} рублей")
        print(f"Статус: Студент")
    
    def calculate_scholarship(self) -> float:
        
        if self.avg_grade == 5:
            return 6000
        elif self.avg_grade < 5 and self.avg_grade >= 3:  # Предположим, что 3 - проходной балл
            return 4000
        else:
            return 0
    
    def scholarship_comparison(self, other: Person) -> str:
       
        if not isinstance(other, Person):
            return "Невозможно сравнить: объект сравнения не является студентом или аспирантом"
        
        my_scholarship = self.calculate_scholarship()
        other_scholarship = other.calculate_scholarship()
        
        if my_scholarship > other_scholarship:
            return f"Стипендия {self.name}({my_scholarship} рублей) выше, чем у {other.name}({other_scholarship} рублей)"
        elif my_scholarship < other_scholarship:
            return f"Стипендия {self.name}({my_scholarship} рублей) ниже, чем у {other.name}({other_scholarship} рублей)"
        else:
            return f"Стипендии {self.name} и {other.name} одинаковы и составляют {my_scholarship} рублей"
    
    def __str__(self) -> str:
        scholarship = self.calculate_scholarship()
        return f"Студент[{self.name}, {self.age} лет, группа {self.group}, средний балл {self.avg_grade:.2f}, стипендия {scholarship} рублей]"


class Aspirant(Student):
    
    def __init__(self, name: str, age: int, group: str, avg_grade: float, research_title: str):
        
        super().__init__(name, age, group, avg_grade)
        
        if not research_title or not isinstance(research_title, str):
            raise ValueError("Название научной работы должно быть непустой строкой")
        
        self.research_title = research_title
    
    def display_info(self) -> None:
        super().display_info()
        print(f"Научная работа: {self.research_title}")
        # Изменяем отображение статуса
        print(f"Статус: Аспирант")
    
    def calculate_scholarship(self) -> float:
        
        if self.avg_grade == 5:
            return 8000
        elif self.avg_grade < 5 and self.avg_grade >= 3:  # Предположим, что 3 - проходной балл
            return 6000
        else:
            return 0
    
    def __str__(self) -> str:
        scholarship = self.calculate_scholarship()
        return f"Аспирант[{self.name}, {self.age} лет, группа {self.group}, средний балл {self.avg_grade:.2f}, работа '{self.research_title}', стипендия {scholarship} рублей]"


def demonstrate_student_system():
    print("Задача 4: Демонстрация системы студентов и аспирантов")
    print("=" * 60)
    
    # Создаем тестовые данные
    people = [
        Student("Иван Иванов", 20, "Группа A", 4.8),
        Student("Мария Петрова", 21, "Группа B", 5.0),
        Student("Алексей Сидоров", 22, "Группа C", 2.5),
        Aspirant("Анна Кузнецова", 25, "Аспирантская группа A", 4.9, "Применение искусственного интеллекта в медицинской диагностике"),
        Aspirant("Дмитрий Смирнов", 26, "Аспирантская группа B", 5.0, "Исследование оптимизации алгоритмов квантовых вычислений"),
        Aspirant("Екатерина Попова", 24, "Аспирантская группа C", 3.2, "Анализ интерпретируемости моделей машинного обучения"),
    ]
    
    # Отображаем информацию о всех людях
    print("Информация о всех людях:")
    print("-" * 50)
    for person in people:
        person.display_info()
        print("-" * 30)
    print()
    
    # Демонстрация сравнения стипендий
    print("Сравнение стипендий:")
    print("-" * 50)
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            comparison_result = people[i].scholarship_comparison(people[j])
            print(f"  {comparison_result}")
    print()


def scholarship_analysis():
    print("Статистический анализ стипендий:")
    print("-" * 50)
    
    # Создаем больше тестовых данных
    students = [
        Student("Студент 1", 20, "Группа A", 4.5),
        Student("Студент 2", 21, "Группа B", 5.0),
        Student("Студент 3", 22, "Группа C", 3.8),
        Student("Студент 4", 23, "Группа D", 2.0),
    ]
    
    aspirants = [
        Aspirant("Аспирант 1", 25, "Аспирантская группа A", 4.8, "Работа 1"),
        Aspirant("Аспирант 2", 26, "Аспирантская группа B", 5.0, "Работа 2"),
        Aspirant("Аспирант 3", 27, "Аспирантская группа C", 3.5, "Работа 3"),
        Aspirant("Аспирант 4", 28, "Аспирантская группа D", 4.0, "Работа 4"),
    ]
    
    all_people = students + aspirants
    
    # Статистическая информация
    total_students = len(students)
    total_aspirants = len(aspirants)
    total_scholarship = sum(person.calculate_scholarship() for person in all_people)
    
    student_scholarship = sum(student.calculate_scholarship() for student in students)
    aspirant_scholarship = sum(aspirant.calculate_scholarship() for aspirant in aspirants)
    
    avg_student_scholarship = student_scholarship / total_students if total_students > 0 else 0
    avg_aspirant_scholarship = aspirant_scholarship / total_aspirants if total_aspirants > 0 else 0
    
    print(f"Количество студентов: {total_students}")
    print(f"Количество аспирантов: {total_aspirants}")
    print(f"Общая стипендия студентов: {student_scholarship} рублей")
    print(f"Общая стипендия аспирантов: {aspirant_scholarship} рублей")
    print(f"Общая стипендия всех: {total_scholarship} рублей")
    print(f"Средняя стипендия студента: {avg_student_scholarship:.2f} рублей")
    print(f"Средняя стипендия аспиранта: {avg_aspirant_scholarship:.2f} рублей")
    print()
    
    # Распределение стипендий
    print("Распределение стипендий:")
    scholarship_levels = [0, 4000, 6000, 8000]
    for level in scholarship_levels:
        count = sum(1 for person in all_people if person.calculate_scholarship() == level)
        print(f"  {level} рублей: {count} человек")
    print()


def interactive_system():
    print("Интерактивная система управления студентами")
    print("=" * 60)
    
    people_db = []  # Простая база данных людей
    
    while True:
        print("\nВыберите операцию:")
        print("1. Добавить студента")
        print("2. Добавить аспиранта")
        print("3. Просмотреть всех")
        print("4. Сравнить стипендии")
        print("5. Статистический анализ")
        print("6. Выйти из системы")
        
        choice = input("Введите выбор (1-6): ").strip()
        
        if choice == '6':
            print("Выход из системы, до свидания!")
            break
        
        try:
            if choice == '1':
                # Добавление студента
                print("\nДобавление нового студента:")
                name = input("Имя: ").strip()
                age = int(input("Возраст: ").strip())
                group = input("Группа: ").strip()
                avg_grade = float(input("Средний балл (0-5): ").strip())
                
                student = Student(name, age, group, avg_grade)
                people_db.append(student)
                print(f"✓ Успешно добавлен: {student}")
                
            elif choice == '2':
                # Добавление аспиранта
                print("\nДобавление нового аспиранта:")
                name = input("Имя: ").strip()
                age = int(input("Возраст: ").strip())
                group = input("Группа: ").strip()
                avg_grade = float(input("Средний балл (0-5): ").strip())
                research_title = input("Название научной работы: ").strip()
                
                aspirant = Aspirant(name, age, group, avg_grade, research_title)
                people_db.append(aspirant)
                print(f"✓ Успешно добавлен: {aspirant}")
                
            elif choice == '3':
                # Просмотр всех людей
                print("\nИнформация о всех людях:")
                if not people_db:
                    print("  База данных пуста")
                else:
                    for i, person in enumerate(people_db, 1):
                        print(f"{i}. ", end="")
                        person.display_info()
                        print("-" * 30)
                        
            elif choice == '4':
                # Сравнение стипендий
                if len(people_db) < 2:
                    print("Необходимо как минимум 2 человека для сравнения")
                    continue
                
                print("\nВыберите людей для сравнения:")
                for i, person in enumerate(people_db, 1):
                    print(f"{i}. {person.name} ({person.__class__.__name__})")
                
                try:
                    idx1 = int(input("Выберите номер первого человека: ")) - 1
                    idx2 = int(input("Выберите номер второго человека: ")) - 1
                    
                    if 0 <= idx1 < len(people_db) and 0 <= idx2 < len(people_db):
                        result = people_db[idx1].scholarship_comparison(people_db[idx2])
                        print(f"\nРезультат сравнения: {result}")
                    else:
                        print("Неверный номер")
                except ValueError:
                    print("Пожалуйста, введите корректное число")
                    
            elif choice == '5':
                # Статистический анализ
                if not people_db:
                    print("База данных пуста")
                    continue
                
                students = [p for p in people_db if isinstance(p, Student) and not isinstance(p, Aspirant)]
                aspirants = [p for p in people_db if isinstance(p, Aspirant)]
                
                print(f"\nСтатистика базы данных:")
                print(f"Всего людей: {len(people_db)}")
                print(f"Студентов: {len(students)}")
                print(f"Аспирантов: {len(aspirants)}")
                
                total_scholarship = sum(p.calculate_scholarship() for p in people_db)
                print(f"Общие расходы на стипендии: {total_scholarship} рублей")
                
            else:
                print("Неверный выбор, попробуйте снова")
                
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Ошибка операции: {e}")


def test_edge_cases():
    print("\nТестирование граничных случаев:")
    print("-" * 50)
    
    # Тестируем неверные входные данные
    test_cases = [
        ("Пустое имя", lambda: Student("", 20, "Группа A", 4.0)),
        ("Неверный возраст", lambda: Student("Тест", -5, "Группа A", 4.0)),
        ("Неверный средний балл", lambda: Student("Тест", 20, "Группа A", 6.0)),
        ("Пустая группа", lambda: Student("Тест", 20, "", 4.0)),
        ("Пустая научная работа аспиранта", lambda: Aspirant("Тест", 25, "Группа A", 4.0, "")),
    ]
    
    for description, test_func in test_cases:
        try:
            test_func()
            print(f"✗ {description}: должно было вызвать исключение, но не вызвало")
        except (ValueError, Exception) as e:
            print(f"✓ {description}: правильно вызвало исключение - {e}")


if __name__ == "__main__":
    
    # Демонстрация базовой функциональности
    demonstrate_student_system()
    
    # Анализ стипендий
    scholarship_analysis()
    
    # Интерактивная система
    interactive_system()
    
    # Тестирование граничных случаев
    test_edge_cases()
    
    print("\n" + "=" * 60)
    print("Задача 4 завершена! Демонстрация системы студентов и аспирантов окончена.")