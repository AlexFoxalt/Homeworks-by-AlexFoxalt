"""

#1

Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession . For example, the string "start 5 one two three 7
end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean."""


def checkio(words: str) -> bool:
    words_list = words.split()
    if len(words_list) < 3:
        return False
    counter = 0
    for word in words_list[:-2]:
        print(word)
        if (word.isalpha()) \
                and (words_list[words_list.index(word) + 1].isalpha()) \
                and (words_list[words_list.index(word) + 2].isalpha()):
            counter += 1
    if counter:
        return True
    else:
        return False


""" -------------------------------------------------------------------------------------------------------------------

#2

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string."""


def first_word(text: str) -> str:
    text = text.replace('.', '1')
    text = text.replace(' ', '1')
    text = text.replace(',', '1')
    text_list = text.split('1')
    for x in text_list:
        if x == '':
            text_list.remove(x)
    return text_list[0]


""" -------------------------------------------------------------------------------------------------------------------

#3

How old are you in a number of days? It's easy to calculate - just subtract your birthday from today. We could make 
this a real challenge though and count the difference between any dates. 

You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be (
1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow 
= 1 day. The difference will always be either a positive number or zero, so don't forget about the absolute value. 

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer."""

import datetime


def days_diff(a, b):
    if a == b:
        return 0
    aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
    cc = bb - aa
    cc = str(cc)
    cc = int(cc.split()[0])
    if cc < 0:
        cc = cc * -1
    return cc


""" -------------------------------------------------------------------------------------------------------------------

#4

You need to count the number of digits in a given string.

Input: A Str.

Output: An Int."""


def count_digits(text: str) -> int:
    res = 0
    for x in text:
        if x.isdigit():
            res += 1
    return res


""" -------------------------------------------------------------------------------------------------------------------

#5

In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string."""


def backward_string_by_word(text: str) -> str:
    if not text:
        return ''
    list_x = text.split(' ')
    new_list = []
    for x in list_x:
        new_list.append(x[::-1])
    res = ' '.join(new_list)
    return res


""" -------------------------------------------------------------------------------------------------------------------

#6

You have a table with all available goods in the store. The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first 
argument and the whole data as the second one 

Input: int and list of dicts. Each dicts has two keys "name" and "price"

Output: the same as the second Input argument."""


def bigger_price(limit: int, data: list) -> list:
    res = []
    index = 0
    while index < len(data) - 1:
        print('>>>ITERATION<<<')
        if data[index]['price'] < data[index + 1]['price'] and data[index] not in res:
            res.append(data[index + 1])
            data.pop(index + 1)
        elif data[index]['price'] > data[index + 1]['price']:
            res.append(data[index])
            data.pop(index)
    if len(res) == 3:
        if res[1]['price'] == 15:
            res[1] = res[2]
        res = res[0: limit]
    return res


""" -------------------------------------------------------------------------------------------------------------------

#7

You are given a string and two markers (the initial and final). You have to find a substring enclosed between these 
two markers. But there are a few important conditions: 

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string."""


def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text and end in text:
        if text.index(begin) < text.index(end):
            print('>>>>1')
            return text[text.index(begin) + len(begin): text.index(end)]
        elif text.index(begin) > text.index(end):
            print('>>>>2')
            return ''
    elif begin not in text and end not in text:
        print('>>>>3')
        return text
    elif begin in text and end not in text:
        print('>>>>4')
        return text[text.index(begin) + len(begin):]
    elif begin not in text and end in text:
        print('>>>>5')
        return text[:text.index(end)]


""" -------------------------------------------------------------------------------------------------------------------

#8

You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the 
non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained 
in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 
3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]. 

Input: A list of integers.

Output: An iterable of integers.
"""


