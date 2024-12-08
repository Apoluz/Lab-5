import re

# Ruta del archivo
file_path = r"C:\Users\marki\Desktop\Descargas_labs\task2.html"

# Expresión regular para encontrar valores en píкселях (ejemplo: 10px, 100px)
pixels_regex = r"\b\d+px\b"

try:
    # Abrir y leer el archivo
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Buscar valores en píкселях
    pixel_values = re.findall(pixels_regex, content)
    
    # Mostrar resultados
    print("Значения в пикселях:")
    for value in pixel_values:
        print(value)

except FileNotFoundError:
    print(f"Файл по пути '{file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
