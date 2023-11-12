# Импортирование библиотек
import sys
import pprint
import re

# Чтение какого-то файла
with open('docs/utf8/128', 'r', -1, 'UTF-8') as file:
    lines = file.readlines()


def clearing_data(text):  # Очистка данных
    """new_text = text.replace(',', '')
    new_text = new_text.replace(':', '')
    new_text = new_text.replace('…', '.')
    new_text = new_text.replace('?', '.')
    new_text = new_text.replace('!', '.')
    new_text = new_text.replace('-', '')
    new_text = new_text.replace('  ', ' ')
    new_text = new_text.replace('“', '')
    new_text = new_text.replace("”", '')
    new_text = new_text.replace("\n", ' ')
    new_text = new_text.replace("(", '')
    new_text = new_text.replace(")", '')
    new_text = new_text.replace("'", '')
    new_text = new_text.replace('"', '')
    new_text = new_text.replace('—', '')
    new_text = new_text.replace('/', '')
    #new_text = re.sub("[,|:|“|”|(|)|'|-|/|—]", "", text)
    #new_text = re.sub("[?|!|...|…|]", ".", new_text)
    #new_text = re.sub("[\n|  |\xa0|]", " ", new_text)
    # В итоге мы в тексте оставляем все буквы, точки и пробелы (исправьте меня, если я что-то забыл)
    new_text = re.sub("[^A-Za-zА-Яа-я.\n ]", '', text)
    new_text = new_text.replace('\n', ' ')
    new_text = new_text.replace(' . ', '')
    new_text = new_text.replace('  ', ' ')
    return new_text
    # В итоге мы в тексте оставляем все буквы, цифры, точки и пробелы (исправьте меня, если я что-то забыл)
    new_text = []
    for i in text:
        if i != '\n':
            fragment = re.sub("[^A-Za-zА-Яа-я.0-9-\n ]", '', i)
            if fragment != '':
                new_text.append(fragment)

    return new_text
    """


# print(clearing_data(lines))
pprint.pprint(clearing_data(lines))
