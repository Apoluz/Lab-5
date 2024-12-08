import re
import csv

# Ruta completa del archivo de entrada
input_file = r"C:\Users\marki\Desktop\Descargas_labs\task3.txt"
# Ruta completa del archivo de salida
output_file = r"C:\Users\marki\Desktop\Descargas_labs\task3_normalized.csv"

# Expresiones regulares para extraer datos
regex_id = r'\b\d+\b'  # IDs: números enteros
regex_email = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'  # Correos electrónicos
regex_date = r'\b\d{4}-\d{2}-\d{2}\b'  # Fechas en formato YYYY-MM-DD
regex_url = r'\bhttps?://[^\s]+\b'  # URLs que empiezan con http o https
regex_surname = r'\b[А-ЯЁA-Z][а-яёa-zA-Z-]+\b'  # Apellidos (latinos y cirílicos)

try:
    # Leer el contenido del archivo
    with open(input_file, "r", encoding="utf-8") as file:
        data = file.read()

    # Extraer datos usando las expresiones regulares
    ids = re.findall(regex_id, data)
    emails = re.findall(regex_email, data)
    dates = re.findall(regex_date, data)
    urls = re.findall(regex_url, data)

    # Extraer apellidos eliminando otros datos ya encontrados
    remaining_data = re.sub(f"{regex_id}|{regex_email}|{regex_date}|{regex_url}", "", data)
    surnames = re.findall(regex_surname, remaining_data)

    # Asegurar que todas las listas tengan la misma longitud
    min_length = min(len(ids), len(surnames), len(emails), len(dates), len(urls))
    ids = ids[:min_length]
    surnames = surnames[:min_length]
    emails = emails[:min_length]
    dates = dates[:min_length]
    urls = urls[:min_length]

    # Guardar los datos en un archivo CSV con codificación utf-8-sig
    with open(output_file, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')  # Usa punto y coma como separador
        writer.writerow(["ID", "Фамилия", "Электронная почта", "Дата регистрации", "Сайт"])
        for i in range(min_length):
            writer.writerow([ids[i], surnames[i], emails[i], dates[i], urls[i]])

    print(f"Данные успешно обработаны и сохранены в файл: '{output_file}'")

except FileNotFoundError:
    print(f"Файл '{input_file}' не найден. Проверьте путь к файлу.")
except Exception as e:
    print(f"Произошла ошибка: {e}")


