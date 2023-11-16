# Импортирование библиотек
import sys
import pprint
import re
import unicodedata
from stop_words import get_stop_words
from pymorphy3 import MorphAnalyzer


morph = MorphAnalyzer()
doc = 143  # файл
# Чтение какого-то файла
with open(f'docs/utf8/{doc}', 'r', -1, 'UTF-8') as file:
    lines = file.read()


def clearing_data(text):  # Очистка данных
    # Убираем неразрывный пробел
    new_text = unicodedata.normalize("NFKD", text)
    new_text = new_text.replace('-', ' ')
    # В тексте оставляем все буквы, цифры, точки и пробелы (исправьте меня, если я что-то забыл)
    new_text = re.sub("[^A-Za-zА-Яа-я\n ]", '', new_text)

    # Теряются несколько точек
    new_text = new_text.replace('\n', ' ')
    return new_text


def changing_case(text):  # Изменение регистра
    return text.lower()


def tokenization(text):  # Токенизация
    return text.split()


def deleting_stop_words(text):  # Удаление стоп-слов
    new_text = []
    stop_words = get_stop_words('russian')
    stop_words1 = get_stop_words('english')
    stop_words = stop_words1 + stop_words
    for i in text:
        if not (i in stop_words):
            new_text.append(i)
    return new_text


def lemmatization(text):  # Лемматизация
    tokens = []
    for i in text:
        tokens.append(morph.parse(i)[0].normal_form)
    return tokens


def word_counter(text):  # Счетчик слов
    # Выводить в порядке убывания!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    words_dict = {}

    for word in text:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return sorted(words_dict.items(), key=lambda item: item[1], reverse=True)

    # sorted_people = sorted(people.items(), key=lambda item: item[1])


def vectorization(text):  # Векторизация
    pass


text = clearing_data(lines)
text = changing_case(text)
text = tokenization(text)
text = deleting_stop_words(text)
text = lemmatization(text)
text = word_counter(text)
pprint.pprint(text)
# print(deleting_stop_words(text))
