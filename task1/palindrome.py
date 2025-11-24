def is_palindrome(s):

    # Если ввод не строка, преобразуем в строку
    if not isinstance(s, str):
        s = str(s)
    
    # Очистка строки: оставляем только буквы и цифры, приводим к нижнему регистру
    cleaned_chars = []
    for char in s:
        if char.isalnum():  # Оставляем только буквы и цифры
            cleaned_chars.append(char.lower())
    
    cleaned_str = ''.join(cleaned_chars)
    
    # Проверяем, является ли палиндромом
    return cleaned_str == cleaned_str[::-1]


def test_palindrome():
    """
    Тестирует функцию палиндрома на различных случаях
    """
    test_cases = [
        # (входная строка, ожидаемый результат)
        ("A man a plan a canal Panama", True),    # Классический палиндром с пробелами
        ("racecar", True),                        # Стандартный палиндром
        ("hello", False),                         # Не палиндром
        ("", True),                               # Пустая строка
        ("a", True),                              # Один символ
        ("12321", True),                          # Числовой палиндром
        ("Was it a car or a cat I saw?", True),   # Палиндром с пунктуацией
        ("Python", False),                        # Не палиндром
        ("Madam", True),                          # Игнорирует регистр
        ("Able was I ere I saw Elba", True),      # Длинный палиндром
    ]
    
    print("Тестирование функции проверки палиндрома:")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = is_palindrome(test_input)
        status = "✓ Пройдено" if result == expected else "✗ Не пройдено"
        
        print(f"Тест {i}: {status}")
        print(f"  Ввод: '{test_input}'")
        print(f"  Ожидается: {expected}, Получено: {result}")
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print()
    
    print("=" * 50)
    print(f"Результаты тестирования: Пройдено {passed}/{len(test_cases)}, Не пройдено {failed}/{len(test_cases)}")
    
    return failed == 0


def interactive_check():
    """
    Интерактивная проверка строки на палиндром
    """
    print("Проверка палиндрома")
    print("Введите 'quit' для выхода из программы")
    print("-" * 30)
    
    while True:
        user_input = input("Введите строку для проверки: ").strip()
        
        if user_input.lower() == 'quit':
            print("Программа завершена, до свидания!")
            break
        
        if is_palindrome(user_input):
            print(f"✓ '{user_input}' является палиндромом!")
        else:
            print(f"✗ '{user_input}' не является палиндромом")
        
        print()


if __name__ == "__main__":
    """
    Главная точка входа программы
    """
    print("Задача 1: Функция проверки палиндрома")
    print("=" * 50)
    
    # Запуск автоматического тестирования
    test_success = test_palindrome()
    
    if test_success:
        print("\nВсе тесты пройдены! Начинаем интерактивную проверку...")
        print()
        interactive_check()
    else:
        print("\nНекоторые тесты не пройдены, пожалуйста, проверьте реализацию кода.")