import re

file_path = "C:\\Users\\marki\\Desktop\\Descargas_labs\\task1-en.txt"

word_with_period_regex = r"\b\w+\."
fractional_numbers_regex = r"\b\d+\.\d+\b"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    
    words_with_period = re.findall(word_with_period_regex, content)
    fractional_numbers = re.findall(fractional_numbers_regex, content)
    
    
    print("Слова, за которыми следует точка:")
    for word in words_with_period:
        print(word)
    
    print("\nДробные числа:")
    for number in fractional_numbers:
        print(number)

except FileNotFoundError:
    print(f"Файл по пути '{file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

