""" Чернышов HW8
Задание №1
В отдельном файле (пусть будет lib.py) написать функцию, которая требует от пользователя
ответить да или нет ( Y/N ) и возвращает True or False в зависимости от того, что он ввел. В основном файле (пусть будет
main_file.py) попросить пользователя ввести с клавиатуры строку и вывести ее на экран. Используя импортированную из
lib.py функцию спросить у пользователя, хочет ли он повторить операцию (Y/N).Повторять пока пользователь отвечает Y и
прекратить когда пользователь скажет N. """

from lib import yes_or_no
from math import sqrt
from random import randint


def repeat_foo(x: str):
    while True:
        restart_or_no = input('Do you want to restart? (yes/no): ')
        restart_or_no = yes_or_no(restart_or_no)
        if restart_or_no == 'Error':
            print('< < < Error > > >')
        elif not restart_or_no:
            break
        else:
            print(f'Your data is: {user_str}')


user_str = input('Enter your data: ')
print(f'Your data is: {user_str}')
repeat_foo(user_str)

"""Задание №2 
Написать функцию принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр 
квадрата, площадь квадрата и диагональ квадрата. Можете воспользоваться модулем math для математики"""


def do_some_geometry_things(x: int):
    perimeter = x * 4
    area = x * x
    diagonal = round(sqrt(2) * x, 2)
    return print(f'Perimeter = {perimeter}, Area = {area}, Diagonal = {diagonal}')


while True:
    user_data = input('Enter the side length of a square: ')
    try:
        user_data = int(user_data)
        do_some_geometry_things(user_data)
        break
    except ValueError:
        print('< < < Error > > >')

"""Задание №3
Напишите "Русскую рулетку". В револьвер заряжается 1 патрон из 6. Спрашиваем пользователя "Стрелять или 
нет ?". Случайным образом определяется патрон. Если заряжен - показываем сообщение "Бабах!" . Если нет - спрашиваем 
"Стрелять или нет ?" и тд.. """


def russian_roulette():
    while True:
        bang_number = 1
        res = randint(1, 6)
        if res == bang_number:
            print('***Boom***\nGame over, you are dead.')
            return
        else:
            print('***Click***\nNot this time!')
            yes_or_no_question = input('One more time? (yes/else=exit): ').lower()
            if yes_or_no_question != 'yes':
                print('Bye bye!')
                return
            else:
                print("Let's Go!")


while True:
    start_or_no = input('Playing Russian Roulette. Do you want to start? (yes/no): ')
    if start_or_no.lower() == 'yes':
        russian_roulette()
        break
    elif start_or_no.lower() == 'no':
        print('Bye Bye!')
        break
    else:
        print('< < < Error > > >')
