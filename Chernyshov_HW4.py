# Чернышов Алексей HW4

# Задание 1
# Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 3, 5, 95, 7, 87, 13, 45, 67, 44,]).
# Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.
# Учтите, что это должен быть именно исходный лист (с тем же id), а не новый.
print('---------------Задание №1---------------')
lst1 = [11, 77, 4, 22, 0, 3, 5, 95, 7, 87, 13, 45, 67, 44]
print('Список без изменений', lst1, 'id:', id(lst1))
ind = 0
while ind < len(lst1):
    if 18 > lst1[ind] or 81 < lst1[ind]:
        del lst1[ind]
    else:
        ind += 1
        pass
print('Список с изменениями', lst1, 'id:', id(lst1))

# Задание 2
# "Искусственный интеллект". Есть строка произвольного содержания. Программа должна сообщить:
# "It's phone number" если строка это телефонный номер ("+" и 12 цифр, напр "+380631112233")
# "It's name" если строка это ФИО (имя и инициалы, например "Ivanov A. B.")
print('---------------Задание №2---------------')
print('Если ваши данные являются номером телефона или Фамилией и иницалами- вам об этом сообщат.'
      '\n***Формат ввода***'
      '\nФамилия и инициалы = Хххххх Х. Х. '  
      '\nНомер телефона = +хххххххххххх')
enter = input('Введите данные: ')
if enter:
    print('Ваши данные:', enter)
elif not enter:
    pass
if len(enter) == 13 and enter.startswith('+'):
    no_plus = enter[1:13]
    if no_plus.isdigit():
        print('Это, однозначно, номер телефона!!!'), exit(0)
    elif not no_plus.isdigit():
        print('Почти номер телефона, но увы :)')
else:
    pass
enter = enter.split()
if len(enter) == 3:
    if enter[1].endswith('.') and enter[2].endswith('.'):
        if enter[0].istitle() and enter[1].istitle() and enter[2].istitle():
            if len(enter[1]) == 2 and len(enter[2]) == 2:
                print('Это, 100%, фамилия и инициалы!!!')
                exit(0)
            else:
                pass
        else:
            pass
    else:
        pass
print('Данные, которые вы ввели, не являются ни номером телефона, ни Фамилией и инициалами. '
      '\nВ следующий раз введите данные в предусмотренном формате. (см. ***Формат ввода***)')

# Задание №3
# Есть строка произвольного содержания. Найти и вывести на экран самое длинное слово в строке, в котором
# присутствуют подряд две согласные буквы.
# Если в строке присутствует слово с тремя согласными буквами подряд - вывести это слово на экран в верхнем регистре.

print('---------------Задание №3---------------')

words_list = input('Введите текст для анализа: ').lower().split()
if not words_list:
    print('Вы ничего не ввели.')
    exit(0)
consonants = 'бвгджзйклмнпрстфхцчшщ'
consonants_list = []
for con in consonants:
    consonants_list.append(con)
x2_list = []
for con1 in consonants_list:
    for con2 in consonants_list:
        x2_of_con = con1 + con2
        for word in words_list:
            if x2_of_con in word:
                x2_list.append(word)
x3_list = []
for con1 in consonants_list:
    for con2 in consonants_list:
        for con3 in consonants_list:
            x3_of_con = con1 + con2 + con3
            for word in words_list:
                if x3_of_con in word:
                    x3_list.append(word)
x2_list_unique = []
for word in x2_list:
    if word not in x3_list and word.isalpha():
        x2_list_unique.append(word)
if x2_list_unique:
    pass
else:
    print('Введенный текст некорректен.')
    exit(0)
res_x2_of_cons = max(x2_list_unique, key=len)
res_x3_of_cons = []
for word_check in x3_list:
    res_x3_of_cons.append(word_check.upper())
if not res_x2_of_cons:
    res_x2_of_cons = '!Таких слов нет!'
elif not res_x3_of_cons:
    res_x3_of_cons = '!Таких слов нет!'
print(f'В вашем тексте:\nСамое длинное слово с двуми согласными подряд: {res_x2_of_cons}'
      f'\nСписок слов с тремя согласными подряд: {res_x3_of_cons}')
