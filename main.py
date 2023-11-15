# Импортирование библиотек
import sys

# Чтение какого-то файла
with open('100.txt', 'r', -1, 'UTF-8') as file:
    lines = file.read()


def clearing_data(text):  # Очистка данных (не доконца)
    new_text = text.replace(',', '')
    new_text = new_text.replace(':', '')
    new_text = new_text.replace('…', '.')
    new_text = new_text.replace('?', '.')
    new_text = new_text.replace('!', '.')
    new_text = new_text.replace('-', '')
    new_text = new_text.replace('  ', ' ')
    new_text = new_text.replace('“', '')
    new_text = new_text.replace("”", '')
    return new_text


print(clearing_data(lines))