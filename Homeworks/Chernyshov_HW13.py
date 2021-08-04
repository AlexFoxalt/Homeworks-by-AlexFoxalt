"""Чернышов HW13"""
import requests

"""Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ), получите текущий курс валют и
 запишите его в TXT-файл в таком формате:
 "[дата создания запроса]"
1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
3. [название ввалюты 3] to UAH: [значение курса к валюте 3]
...
n. [название ввалюты n] to UAH: [значение курса к валюте n]"""

my_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

try:
    res = requests.get(my_url)
except Exception as error:
    print(error)

try:
    with open('Currency.txt', 'w') as txt_file:
        txt_file.write(res.headers['Date'])
        for num, value in enumerate(res.json()):
            num = str(num + 1) + '.'
            txt_file.write('\n' + num + value['txt'] + ' to UAH: ' + str(value['rate']))
except Exception as error:
    print(error)

"""2. * Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны к этой валюте за 
указаную дату используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП!"""


class Money:
    my_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'

    def __init__(self, date: str, cc: str):
        """date format: YEARMONTHDAY(ex.'20201010') , cc format: STR(ex.'EUR') """
        if isinstance(cc, str) and len(cc) == 3:
            self.cc = cc.upper()
        else:
            raise Exception('Incorrect data')
        if isinstance(date, str) and len(date) == 8 and date.isdigit():
            self.date = date
        else:
            raise Exception('Incorrect data')

        try:
            self.data = requests.get(self.my_url, params={'date': self.date, 'format': 'json'})
        except Exception as error:
            print(error)

    def currency(self):
        """Main func, will show you actual currency on your date"""
        if len(self.data.json()) == 1:
            raise Exception('Incorrect data')
        try:
            for data in self.data.json():
                if data['cc'] == self.cc:
                    val = data['rate']
                    date = data['exchangedate']
            print(f'The {self.cc} to UAH exchange rate on {date} is {val}')
        except Exception as error:
            print(error)

    def cc_list(self):
        """If you want to know all possible cc's in this bank"""
        print(list(data['cc'] + " = " + data['txt'] for data in self.data.json()))


ex1 = Money('20210804', 'EUR')
ex2 = Money('20070909', 'USD')

ex1.currency()
ex2.currency()  # Как же было хорошо

ex1.cc_list()

# freak = Money(123 , False)
