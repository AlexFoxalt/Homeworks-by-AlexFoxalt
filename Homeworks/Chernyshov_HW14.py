"""Чернышов HW14"""
import re

"""
Задание №1
Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AA1234BB, 12 123-45AB, a12345BC) с 
помощью регулярных выражений. Функция принимает строку и возвращает None если вся строка не является номерным знаком. 
Если является номерным знаком - возвращает саму строку."""

type1 = re.compile(r'[А-ЯA-Z]{2}\d{4}[А-ЯA-Z]{2}')
type2 = re.compile(r'\d{2} \d{3}-\d{2}[А-ЯA-Z]{2}')
type3 = re.compile(r'[а-яa-z]\d{5}[А-ЯA-Z]{2}')
TYPES_LIST = [type1, type2, type3]


def find_license_plate(text):
    global TYPES_LIST
    for type_latin in TYPES_LIST:
        content = type_latin.search(text)
        if content:
            return f'Найдено: {content.group()} в {content.span()}'
    return 'Ничего не найдено'


some_string1 = 'Продаю машину с гос. номером AA1234BB'
some_string2 = 'Продаю мопед, гос.номер - 12 123-45АВ'
some_string3 = 'Потерял номера a12345ВС, прошу вернуть за вознаграждение'
some_string4 = '11BHBH11 вн0001вн ВН11 11ВН ВНВНВНВН Вн1111ВН'
print(find_license_plate(some_string1))
print(find_license_plate(some_string2))
print(find_license_plate(some_string3))
print(find_license_plate(some_string4))
print('~' * 100)

"""Задание №2
* Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в виде пронумерованного 
списка с помощью регулярных выражений."""


class Plates:
    def __init__(self, text):
        if isinstance(text, str):
            self.text = text
        else:
            raise Exception('Not str type')

    def class_find_license_plate(self):
        global TYPES_LIST
        container = []
        for standard in TYPES_LIST:
            for symbol in standard.findall(self.text):
                container.append(symbol)
        res = []
        for num, item in enumerate(container):
            res.append(str(num + 1) + ': ' + item)
        return res if res else 'Ничего не найдено'


some_text_RUS = 'Мои номера-ВН1111ВН, а мои номера-ВН2222ВН, и мои номера а12345ВС, твои номера 12 123-45АВ?'
some_text_LAT = 'Мои номера-BH1111BH, а мои номера-BH2222BH, и мои номера a12345BC, твои номера 12 123-45AB?'
some_text_TRASH = '11BHBH11 вн0001вн ВН11 11ВН ВНВНВНВН Вн1111ВН'
some_string5 = Plates(some_text_RUS)
some_string6 = Plates(some_text_LAT)
some_string7 = Plates(some_text_TRASH)
print(some_string5.class_find_license_plate())
print(some_string6.class_find_license_plate())
print(some_string7.class_find_license_plate())

"""Задание №3
** Создайте репозиторий на GitLab или GitHub. Сохраните отдельной веткой (пусть будет HW14) 
дз по регулярным выражениям"""

#  Выполнено
