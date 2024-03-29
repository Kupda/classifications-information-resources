# рис. - 143
# свой - 100
# 102 файл надо посмотреть
# И очистку данных

# Импортирование библиотек
import pprint
import re
import unicodedata
from stop_words import get_stop_words
from pymorphy3 import MorphAnalyzer
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import snowball


nltk.download('punkt')
morph = MorphAnalyzer()
doc = 102
with open(f'docs/utf8/{doc}', 'r', -1, 'UTF-8') as file:
    lines = file.read()


def clearing_data(text):  # Очистка данных
    new_text = unicodedata.normalize("NFKD", text)
    new_text = re.sub("[^A-Za-zА-Яа-я]", ' ', new_text)
    return new_text


def changing_case(text):  # Изменение регистра
    return text.lower()


def tokenization(text):  # Токенизация
    return word_tokenize(text, language="russian")


def deleting_stop_words(text):  # Удаление стоп-слов
    new_text = []
    stop_words = get_stop_words('russian')
    for i in text:
        if not (i in stop_words) and len(i) != 1:
            new_text.append(i)
    return new_text


def stemming(text):
    stemmer = snowball.RussianStemmer()
    new_text = []
    for i in text:
        new_text.append(stemmer.stem(i))
    return new_text


def lemmatization(text):  # Лемматизация
    tokens = []
    for i in text:
        p = morph.parse(i)[0]
        if p.tag.POS != 'VERB' and p.tag.POS != 'INFN':
            tokens.append(morph.parse(i)[0].normal_form)
    return tokens
    #lemmatize = nltk.WordNetLemmatizer()
    #text = [lemmatize.lemmatize(word) for word in i]
    #return text


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
#text = stemming(text)
text = lemmatization(text)
text = deleting_stop_words(text)
text = word_counter(text)
pprint.pprint(text)
# print(deleting_stop_words(text))
