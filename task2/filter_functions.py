def filter_strings(filter_lambda, string_array):

    # Проверка входных данных
    if not callable(filter_lambda):
        raise TypeError("filter_lambda должен быть вызываемой функцией")
    
    if not isinstance(string_array, list):
        # Пытаемся преобразовать в список
        try:
            string_array = list(string_array)
        except:
            raise TypeError("string_array должен быть списком или итерируемым объектом")
    
    # Используем функцию filter и lambda для фильтрации
    filtered_result = list(filter(filter_lambda, string_array))
    
    return filtered_result


def demonstrate_filters():
    
    # Тестовые данные
    test_strings = [
        "apple",
        "banana",
        "cherry pie",
        "date",
        "elderberry",
        "fig",
        "grape fruit",
        "honeydew melon",
        "ice cream",
        "jackfruit",
        "kiwi",
        "lemon",
        "mango",
        "nut",
        "orange",
        "pineapple",
        "quince",
        "raspberry",
        "strawberry shortcake",
        "tangerine",
        "umbrella",
        "vanilla",
        "watermelon",
        "xigua",  # китайское слово "арбуз" в пиньине
        "yam",
        "zucchini"
    ]
    
    print("Задача 2: Использование Lambda-функций для фильтрации массива строк")
    print("=" * 60)
    print(f"Исходный массив ({len(test_strings)} элементов):")
    print(test_strings)
    print()
    
    # Условие фильтрации 1: исключить строки, содержащие пробелы
    print("1. Исключить строки, содержащие пробелы:")
    print("-" * 40)
    no_spaces_filter = lambda s: ' ' not in s
    no_spaces_result = filter_strings(no_spaces_filter, test_strings)
    print(f"Lambda-функция: lambda s: ' ' not in s")
    print(f"Результат фильтрации ({len(no_spaces_result)} элементов): {no_spaces_result}")
    print()
    
    # Условие фильтрации 2: исключить строки, начинающиеся с буквы "a" (без учета регистра)
    print("2. Исключить строки, начинающиеся с буквы 'a':")
    print("-" * 40)
    no_a_start_filter = lambda s: not s.lower().startswith('a')
    no_a_start_result = filter_strings(no_a_start_filter, test_strings)
    print(f"Lambda-функция: lambda s: not s.lower().startswith('a')")
    print(f"Результат фильтрации ({len(no_a_start_result)} элементов): {no_a_start_result}")
    print()
    
    # Условие фильтрации 3: исключить строки длиной менее 5 символов
    print("3. Исключить строки длиной менее 5 символов:")
    print("-" * 40)
    min_length_filter = lambda s: len(s) >= 5
    min_length_result = filter_strings(min_length_filter, test_strings)
    print(f"Lambda-функция: lambda s: len(s) >= 5")
    print(f"Результат фильтрации ({len(min_length_result)} элементов): {min_length_result}")
    print()
    
    # Демонстрация комбинированной фильтрации
    print("4. Комбинированная фильтрация: исключить пробелы, длина>=5 и не начинается с 'a'")
    print("-" * 40)
    combined_filter = lambda s: (' ' not in s) and (len(s) >= 5) and (not s.lower().startswith('a'))
    combined_result = filter_strings(combined_filter, test_strings)
    print(f"Lambda-функция: lambda s: (' ' not in s) and (len(s) >= 5) and (not s.lower().startswith('a'))")
    print(f"Результат фильтрации ({len(combined_result)} элементов): {combined_result}")
    print()


def custom_filter_demo():
   
    print("5. Демонстрация пользовательской фильтрации")
    print("-" * 40)
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    
    # Пользовательское условие фильтрации: только строки, начинающиеся с гласной буквы
    vowel_start_filter = lambda s: s[0].lower() in 'aeiou'
    vowel_result = filter_strings(vowel_start_filter, fruits)
    print(f"Строки, начинающиеся с гласной буквы: {vowel_result}")
    
    # Пользовательское условие фильтрации: строки, содержащие букву "e"
    contains_e_filter = lambda s: 'e' in s.lower()
    contains_e_result = filter_strings(contains_e_filter, fruits)
    print(f"Строки, содержащие букву 'e': {contains_e_result}")
    
    print()


def interactive_filtering():
    
    print("6. Интерактивная фильтрация строк")
    print("-" * 40)
    print("Введите список строк (разделенных запятыми):")
    
    try:
        user_input = input("Строки: ").strip()
        if user_input:
            user_strings = [s.strip() for s in user_input.split(',')]
        else:
            user_strings = ["hello", "world", "python", "java", "c++", "git hub"]
            print(f"Используются строки по умолчанию: {user_strings}")
        
        print("\nДоступные условия фильтрации:")
        print("1. Исключить строки, содержащие пробелы")
        print("2. Исключить строки, начинающиеся с 'a'")
        print("3. Исключить строки длиной менее 5 символов")
        print("4. Пользовательское lambda-выражение")
        
        choice = input("\nВыберите условие фильтрации (1-4): ").strip()
        
        if choice == '1':
            result = filter_strings(lambda s: ' ' not in s, user_strings)
            print(f"Результат после исключения пробелов: {result}")
        elif choice == '2':
            result = filter_strings(lambda s: not s.lower().startswith('a'), user_strings)
            print(f"Результат после исключения строк, начинающихся с 'a': {result}")
        elif choice == '3':
            result = filter_strings(lambda s: len(s) >= 5, user_strings)
            print(f"Результат после исключения строк длиной <5: {result}")
        elif choice == '4':
            lambda_expr = input("Введите lambda-выражение (например: 'lambda s: len(s) > 3'): ").strip()
            try:
                # Безопасная оценка lambda-выражения
                if lambda_expr.startswith('lambda'):
                    filter_func = eval(lambda_expr)
                    result = filter_strings(filter_func, user_strings)
                    print(f"Результат пользовательской фильтрации: {result}")
                else:
                    print("Ошибка: lambda-выражение должно начинаться с 'lambda'")
            except Exception as e:
                print(f"Ошибка: неверное lambda-выражение - {e}")
        else:
            print("Неверный выбор")
            
    except Exception as e:
        print(f"Ошибка ввода: {e}")


def test_edge_cases():
    
    print("\n7. Тестирование граничных случаев")
    print("-" * 40)
    
    # Тест пустого списка
    empty_list = []
    result = filter_strings(lambda s: len(s) > 0, empty_list)
    print(f"Фильтрация пустого списка: {result}")
    
    # Тест строк со специальными символами
    special_strings = ["", " ", "  ", "a", "A", "123", "!@#", "hello world"]
    print(f"Список специальных строк: {special_strings}")
    
    # Фильтрация непустых строк
    non_empty = filter_strings(lambda s: len(s.strip()) > 0, special_strings)
    print(f"Непустые строки: {non_empty}")
    
    # Тест обработки ошибок
    try:
        filter_strings("not a function", ["test"])
    except TypeError as e:
        print(f"Тест обработки ошибок - ожидаемая ошибка: {e}")


if __name__ == "__main__":
    
    # Демонстрация базовой функциональности фильтрации
    demonstrate_filters()
    
    # Демонстрация пользовательской фильтрации
    custom_filter_demo()
    
    # Интерактивная фильтрация
    interactive_filtering()
    
    # Тестирование граничных случаев
    test_edge_cases()
    
    print("\n" + "=" * 60)
    print("Задача 2 завершена! Все функции фильтрации продемонстрированы.")