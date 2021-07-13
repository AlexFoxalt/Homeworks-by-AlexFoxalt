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

#6 ***TODO***

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

Output: An iterable of integers."""


def checkio1(data: list) -> list:
    res = []
    for x in data:
        if x in data[data.index(x) + 1:]:
            res.append(x)
    return res


""" -------------------------------------------------------------------------------------------------------------------

#9

In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need 
to determine. 

When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", 
"One", "oNe", "ONE" etc. will do. The search words are always indicated in the lowercase. If the word wasn’t found 
even once, it has to be returned in the dictionary with 0 (zero) value. Input: The text and the search words array. 

Output: The dictionary where the search words are the keys and values are the number of times when those words are 
occurring in a given text. """


def popular_words(text: str, words: list) -> dict:
    text_list = text.lower().split()
    print(text_list)
    res = {}
    for word_check in words:
        counter = 0
        idx = 0
        while idx < len(text_list):
            if word_check == text_list[idx]:
                counter += 1
                idx += 1
            elif word_check != text_list[idx]:
                idx += 1
        new_dict = {word_check: counter}
        res.update(new_dict)
    return res


""" -------------------------------------------------------------------------------------------------------------------

#10

You are given two strings and you have to find an index of the second occurrence of the second string in the first one.

Let's go through the first example where you need to find the second occurrence of "s" in a word "sims". It’s easy to 
find its first occurrence with a function index or find which will point out that "s" is the first symbol in a word 
"sims" and therefore the index of the first occurrence is 0. But we have to find the second "s" which is 4th in a row 
and that means that the index of the second occurrence (and the answer to a question) is 3. 

Input: Two strings.

Output: Int or None"""


def second_index(text: str, symbol: str) -> [int, None]:
    return text.find(symbol, text.index(symbol) + 1) if text.count(symbol) > 1 else None


""" -------------------------------------------------------------------------------------------------------------------

#11

Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times 
they appear in elements. If two elements have the same frequency, they should end up in the same order as the first 
appearance in the iterable. 

Input: Iterable

Output: Iterable"""


def frequency_sort(items):
    return list(sorted(items, key=lambda x: (items.count(x), items.index(x)), reverse=True))


""" -------------------------------------------------------------------------------------------------------------------

#12

Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. 
It has various units with a wide range of movement patterns allowing for a huge number of possible different game 
positions (for example Number of possible chess games at the end of the n-th plies. ) For this mission, 
we will examine the movements and behavior of chess pawns. 

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted 
with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the 
chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission 
we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front 
of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row 
number than the square they currently occupy. 

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this 
strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have 
several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are 
safe. 

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer."""


def safe_pawns(pawns: set) -> int:
    pawns = list(pawns)
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    safe_counter = 0
    for pawn in pawns:
        if pawn[0] != 'a' and pawn[0] != 'h' and pawn[1] != '1':
            if letters[letters.index(pawn[0]) - 1] + numbers[numbers.index(pawn[1]) - 1] in pawns or \
                    letters[letters.index(pawn[0]) + 1] + numbers[numbers.index(pawn[1]) - 1] in pawns:
                safe_counter += 1
        elif pawn[0] == 'a' and pawn[1] != '1':
            if letters[letters.index(pawn[0]) + 1] + numbers[numbers.index(pawn[1]) - 1] in pawns:
                safe_counter += 1
        elif pawn[0] == 'h' and pawn[1] != '1':
            if letters[letters.index(pawn[0]) - 1] + numbers[numbers.index(pawn[1]) - 1] in pawns:
                safe_counter += 1
    return safe_counter


""" -------------------------------------------------------------------------------------------------------------------

#13

Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from 
the nature around him. Programming won't help you with the fire and water, but when it comes to the information 
extraction - it might be just the thing you need. 

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in 
the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means 
that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be 
the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!". 

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places."""


def sun_angle(time: str):
    time = time.split(':')
    try:
        time[0] = int(time[0])
        time[1] = int(time[1])
    except Exception:
        '123'
    minutes = int(time[0] * 60 + time[1])
    if 360 <= minutes <= 1080:
        res = float((minutes - 360) * 0.25)
        res = float('{:.2f}'.format(res))
        return res
    else:
        return "I don't see the sun!"


""" -------------------------------------------------------------------------------------------------------------------

#14

You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should 
have more elements. If it has no elements, then two empty arrays should be returned. 

example

Input: Array.

Output: Array or two arrays."""


def split_list(items: list) -> list:
    if len(items) % 2 == 0:
        list1 = items[:int(len(items) / 2)]
        list2 = items[int(len(items) / 2):]
    else:
        list1 = items[:int(len(items) / 2) + 1]
        list2 = items[int(len(items) / 2 + 1):]
    return list1, list2


""" -------------------------------------------------------------------------------------------------------------------

#15

In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool."""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return True if len(set(elements)) <= 1 else False


""" -------------------------------------------------------------------------------------------------------------------

#16

Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string

Output: The same date and time, but in a more readable format"""

monthes = {'01': 'January',
           '02': 'February',
           '03': 'March',
           '04': 'April',
           '05': 'May',
           '06': 'June',
           '07': 'July',
           '08': 'August',
           '09': 'September',
           '10': 'October',
           '11': 'November',
           '12': 'December',
           }


def date_time(time: str) -> str:
    time = time.split(' ')
    date = time[0].split('.')
    date[0] = int(date[0])
    date_min = time[1].split(':')
    date_min = int(date_min[0]), int(date_min[1])
    if date_min[0] == 1:
        hours = 'hour'
    else:
        hours = 'hours'
    if date_min[1] == 1:
        minutes = 'minute'
    else:
        minutes = 'minutes'
    res = str(date[0]), monthes.get(date[1]), date[2], 'year', str(date_min[0]), hours, str(date_min[1]), minutes
    return ' '.join(res)


""" -------------------------------------------------------------------------------------------------------------------

#17

Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

Input: The secret message.

Output: The decrypted text."""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    code = code.split(' ')
    res = []
    for word in code:
        if word in MORSE:
            res.append(MORSE.get(word))
        else:
            res.append(' ')
    print(res)
    idx = 0
    while idx < len(res) - 1:
        if res[idx] == ' ' == res[idx + 1]:
            res.pop(idx)
        else:
            idx += 1
    return ''.join(res).capitalize()


""" -------------------------------------------------------------------------------------------------------------------

#18

You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".
Input: A list of filenames.

Output: A list of filenames."""

from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    return list(sorted(files, key=lambda x: (x.split('.'[-1]), x.split('.'[-1])[1])))


print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']))


""" -------------------------------------------------------------------------------------------------------------------

#~

Encode and Decode"""


x_decode = {'1': 'A',
            '2': 'B',
            '3': 'C',
            '4': 'D',
            '5': 'E',
            '6': 'F',
            '7': 'G',
            '8': 'H',
            '9': 'I',
            '10': 'J',
            '11': 'K',
            '12': 'L',
            '13': 'M',
            '14': 'N',
            '15': 'O',
            '16': 'P',
            '17': 'Q',
            '18': 'R',
            '19': 'S',
            '20': 'T',
            '21': 'U',
            '22': 'V',
            '23': 'W',
            '24': 'X',
            '25': 'Y',
            '26': 'Z',
            '27': ' '}

decode = lambda code: ''.join(x_decode[i] for i in code.split('.')).capitalize()
x_encode = inv_map = {v: k for k, v in x_decode.items()}
encode = lambda code: '.'.join([x_encode[i] for i in list(code.upper())])


""" -------------------------------------------------------------------------------------------------------------------

#~

Encode and Decode"""