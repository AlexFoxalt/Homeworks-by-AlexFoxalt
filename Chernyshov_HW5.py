"""Чернышов Алексей HW5"""

""" Задание 1
Написать функцию, принимающую один аргумент.
Функция должна вывести на экран тип данных этого аргумента (используйте type)"""


def show_me_type(data1):
    return f'Type of your data: {type(data1)}'


""" Задание 2
Написать функцию, принимающую два аргумента. Функция должна :
- если оба аргумента относятся к числовым типам - вернуть их произведение,
- если к строкам - соединить в одну строку и вернуть,
- если первый строка, а второй нет - вернуть словарь (dict), в котором ключ - первый аргумент, значение - второй
в любом другом случае вернуть кортеж (tuple) из аргументов """


def type_of_data(arg1, arg2):
    if isinstance(arg1, int) and isinstance(arg2, int) or isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    elif isinstance(arg1, str):
        return {arg1: arg2}
    else:
        return arg1, arg2


""" Задание 3
Дан словарь продавцов и цен на какой то товар у разных продавцов: 
{ ‘citrus’: 47.999, ‘istudio’ 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988, ‘sota’: 37.720 }. 
Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон ( верхняя и нижняя граница цены). 
Функция должна принимать словарь с ценами, начало и конец диапазона и возвращать список (list) имен."""


def compare_prices(stores, begin, end):
    result = []
    for key, price in stores.items():
        if begin <= price <= end:
            result.append(key)
    return result


""" Задание 4
* Пользователь вводит строку произвольной длины. Написать функцию, которая должна вернуть словарь следующего содержания: 
ключ - количество букв в слове, значение - список слов с таким количеством букв. 
Отдельным ключем, например "0", записать количество пробелов. Отдельным ключем, 
например "punctuation", записать все уникальные знаки препинания, которые есть в тексте. """


PUNCTUATION_SYMBOLS = '.', ',', '!', '?', ':', ';', '"', '-'


def letter_counter(x: str):
    dict_of_counter_letters = {}
    for word in x.split(' '):
        if word.startswith(PUNCTUATION_SYMBOLS):
            word = word[1:]
        if word.endswith(PUNCTUATION_SYMBOLS):
            word = word[:-1]
        if not len(word) in dict_of_counter_letters:
            dict_of_counter_letters[len(word)] = [word]
        else:
            dict_of_counter_letters[len(word)] += [word]
    return dict_of_counter_letters


def space_counter(x: str):
    counter_of_spaces = 0
    for symbol in x:
        if symbol == ' ':
            counter_of_spaces += 1
    return f'In your text: {counter_of_spaces} space symbols'


def punctuation_counter(x: str):
    counter_of_punctuation = 0
    for symbol in x:
        if symbol in PUNCTUATION_SYMBOLS:
            counter_of_punctuation += + 1
    return f'In your text: {counter_of_punctuation} punctuation symbols'


def lets_count_them_all(x: str):
    res = letter_counter(x)
    space_dict = dict.fromkeys([0], space_counter(x))
    punctuation_dict = dict.fromkeys(['punctuation'], punctuation_counter(x))
    res.update(space_dict)
    res.update(punctuation_dict)
    return res
