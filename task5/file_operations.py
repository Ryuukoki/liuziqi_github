import os
import time
from typing import Tuple, Optional


def create_sample_input_file() -> bool:
    try:
        with open("input.txt", 'w', encoding='utf-8') as f:
            f.write("15.5\n")
            f.write("23.7\n")
        print("Создан пример файла input.txt")
        return True
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        return False


def validate_input_file(filename: str = "input.txt") -> bool:
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не существует")
        return False
    
    if os.path.getsize(filename) == 0:
        print(f"Файл '{filename}' пуст")
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            valid_numbers = 0
            for line in lines:
                stripped = line.strip()
                if stripped:
                    try:
                        float(stripped)
                        valid_numbers += 1
                    except ValueError:
                        continue
            
            if valid_numbers >= 2:
                print(f"Файл '{filename}' действителен, содержит {valid_numbers} чисел")
                return True
            else:
                print(f"Файл '{filename}' требует минимум 2 действительных числа, но найдено только {valid_numbers}")
                return False
    except Exception as e:
        print(f"Ошибка при проверке файла: {e}")
        return False


def display_file_info():
    """Отображает информацию о файлах в текущей директории"""
    print("Информация о файлах в текущей директории:")
    for file in os.listdir('.'):
        if file.endswith(('.py', '.txt')):
            size = os.path.getsize(file)
            print(f"   {file} ({size} байт)")