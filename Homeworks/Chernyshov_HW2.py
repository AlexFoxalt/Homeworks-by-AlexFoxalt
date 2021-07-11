# Чернышов Алексей HW2

# Задание 1
# Используя переменные a и b сформировать строку "First variable is [тут знаение переменной a],
# second variable is [тут знаение переменной b]. Their sum is [тут их вычисленная сумма]."
# Переменные получите с помощью input() или воспользуйтесь константой

a = int(input('First variable is: '))
b = int(input('Second variable is: '))
res = a + b
print('Their sum is', res)


# Задание 2
# Попросить ввести из консоли возраст пользователя. ()
# если пользователь ничего не ввел (или получена пустая строка) - вывести “не понимаю”
# если пользователю меньше 7 - вывести “где твои мама и папа?”
# если пользователю меньше 18 - вывести “мы не продаем сигареты несовершеннолетним”
# если пользователю больше 65 - вывести “вы в зоне риска”
# в любом другом случае - вывести “оденьте маску! ”

age = input('Введите свой возраст: ')
try:
    age = int(age)
    if age < 7 and age != 0:
        print("Где твои мама и папа?")
    elif age < 18 and age != 0:
        print("Мы не продаём сигареты несовершеннолетним.")
    elif 65 < age < 100 and age != 0:
        print("Вы в зоне риска.")
    elif 100 <= age < 120 and age != 0:
        print("Вы везунчик :)")
    elif age > 120 or age == 0:
        print("Не смешно!")
    else:
        print("Наденьте маску.")
except ValueError:
    print('Я не понимаю, введите целое число.')


# Задание 3
# * Усложнение задания 2, сделайте отдельным заданием в этом же файле. Попросить пользователя ввести
# из консоли свой возраст с помощью input(). На место [year] нужно поставить правильный падеж
# существительного "год", который зависит от значения x.
# если пользователь ничего не ввел (ввел пустую строку) - вывести “не понимаю”
# если пользователю меньше 7 - вывести “Тебе [x] [year], где твои мама и папа?”
# если пользователю меньше 18 - вывести “Тебе [x] [year], а мы не продаем сигареты несовершеннолетним”
# если пользователю больше 65 - вывести “Вам уже [x] [year], вы в зоне риска”
# в любом другом случае - вывести “Оденьте маску, вам же всетаки [x] [year]!”


age = input('Введите свой возраст: ')
try:
    age = int(age)
    if age < 7 and age != 0:
        if age == 1:
            year = "год"
        elif 2 <= age <= 4:
            year = "года"
        elif age == 5 or 6:
            year = "лет"
        print(f"Тебе {age} {year}! Где твои мама и папа?")
    elif age < 18 and age != 0:
        if 7 <= age <= 17:
            year = "лет"
        print(f"Тебе {age} {year}, а мы не продаём сигареты несовершеннолетним.")
    elif 65 < age < 100 and age != 0:
        if age % 10 == 1:
            year = "год"
        elif (age % 10 > 1) and (age % 10 < 5):
            year = "года"
        else:
            year = "лет"
        print(f"Вам уже {age} {year}! Вы в зоне риска.")
    elif 100 <= age <= 120 and age != 0:
        if age % 10 == 1:
            year = "года"
        else:
            year = "лет"
        print(f"Вы везунчик :), дожить до {age} {year} это невероятно!")
    elif age > 120 or age == 0:
        print(f"Не смешно! Вам не может быть столько лет!")
    else:
        if age % 10 == 1:
            year = "год"
        elif (age % 10 > 1) and (age % 10 < 5):
            year = "года"
        else:
            year = "лет"
        print(f"Наденьте маску, вам же все таки {age} {year}!")
except ValueError:
    print('Я не понимаю, введите целое число.')