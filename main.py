# Импортирование библиотек
import sys
import pprint
import re
import unicodedata


doc = 143  # файл
# Чтение какого-то файла
with open(f'docs/utf8/{doc}', 'r', -1, 'UTF-8') as file:
    lines = file.read()


def clearing_data(text):  # Очистка данных
    # Убираем неразрывный пробел
    new_text = unicodedata.normalize("NFKD", text)

    # В тексте оставляем все буквы, цифры, точки и пробелы (исправьте меня, если я что-то забыл)
    new_text = re.sub("[^A-Za-zА-Яа-я.0-9-\n!? ]", '', new_text)

    # Теряются несколько точек
    new_text = new_text.replace('\n', ' ')
    return new_text


def changing_case(text):  # Изменение регистра
    return text.lower()


def tokenization(text):  # Токенизация
    pass


def deleting_stop_words(text):  # Удаление стоп-слов
    pass


def lemmatization(text):  # Лемматизация
    pass


def vectorization(text):  # Векторизация
    pass


text = clearing_data(lines)
text = changing_case(text)
pprint.pprint(text)