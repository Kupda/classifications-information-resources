# Импортирование библиотек
import sys
import pprint
import re
import unicodedata

# Чтение какого-то файла
with open('docs/utf8/143', 'r', -1, 'UTF-8') as file:
    lines = file.read()


def clearing_data(text):  # Очистка данных
    # Убираем неразрывный пробел
    new_text = unicodedata.normalize("NFKD", text)

    # В тексте оставляем все буквы, цифры, точки и пробелы (исправьте меня, если я что-то забыл)
    new_text = re.sub("[^A-Za-zА-Яа-я.0-9-\n ]", '', new_text)

    # Теряются несколько точек
    new_text = new_text.replace('\n', ' ')
    return new_text


pprint.pprint(clearing_data(lines))

