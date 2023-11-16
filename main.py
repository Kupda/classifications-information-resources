# рис. - 143
# свой - 100
#

# Импортирование библиотек
import pprint
import re
import unicodedata
from stop_words import get_stop_words
from pymorphy3 import MorphAnalyzer


morph = MorphAnalyzer()
doc = 100
with open(f'docs/utf8/{doc}', 'r', -1, 'UTF-8') as file:
    lines = file.read()


def clearing_data(text):  # Очистка данных
    new_text = unicodedata.normalize("NFKD", text)
    new_text = new_text.replace('-', ' ')
    new_text = new_text.replace('.', ' ')
    new_text = new_text.replace('@', ' ')
    new_text = new_text.replace('_', ' ')
    new_text = re.sub("[^A-Za-zА-Яа-я\n ]", '', new_text)
    new_text = new_text.replace('\n', ' ')
    return new_text


def changing_case(text):  # Изменение регистра
    return text.lower()


def tokenization(text):  # Токенизация
    return text.split()


def deleting_stop_words(text):  # Удаление стоп-слов
    new_text = []
    stop_words = get_stop_words('russian')
    for i in text:
        if not (i in stop_words) and len(i) != 1:
            new_text.append(i)
    return new_text


def lemmatization(text):  # Лемматизация
    tokens = []
    for i in text:
        p = morph.parse(i)[0]
        if p.tag.POS != 'VERB' and p.tag.POS != 'INFN':
            #if i == 'года':
                tokens.append(morph.parse(i)[0].normal_form)
                #print(morph.parse(i)[0].normal_form)
    return tokens


def word_counter(text):  # Счетчик слов
    words_dict = {}

    for word in text:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return sorted(words_dict.items(), key=lambda item: item[1], reverse=True)


def vectorization(text):  # Векторизация
    pass


text = clearing_data(lines)
text = changing_case(text)
text = tokenization(text)
text = lemmatization(text)
text = deleting_stop_words(text)
text = word_counter(text)
pprint.pprint(text)
# print(deleting_stop_words(text))
