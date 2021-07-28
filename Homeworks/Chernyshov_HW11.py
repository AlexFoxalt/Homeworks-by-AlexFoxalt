"""Чернышов Алексей HW11"""

from datetime import datetime

""" Задание №1
Модифицируйте класс Point с занятия. Реализуйте передачу в X и Y только числовых значений. Модифицируйте класс Line 
с занятия следующим образом - обеспечьте проверку точек начала и конца - координаты точек начала и конца отрезка не 
должны совпадать."""


class Point:
    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        ###############################################
        if isinstance(x, int) and isinstance(y, int):
            self.x_coord = x
            self.y_coord = y
        else:
            raise TypeError('Not int')
        ###############################################

    def __str__(self):
        return f'Point {self.x_coord}, {self.y_coord}'


point1 = Point(0, 1)
point2 = Point(0, 0)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


class Line:
    first_point = None
    second_point = None

    def __init__(self, p1, p2):
        if isinstance(p1, Point) and isinstance(p2, Point):
            self.first_point = p1
            self.second_point = p2
            """Можно так"""
            #########################################################################################
            if [self.first_point.x_coord, self.first_point.y_coord] == [self.second_point.x_coord,
                                                                        self.second_point.y_coord]:
                first_point = None
                second_point = None
                raise Exception('point1 == point2')
            #########################################################################################
        else:
            raise Exception('not int')

    def length(self):
        x = (self.first_point.x_coord - self.second_point.x_coord) ** 2
        y = (self.first_point.y_coord - self.second_point.y_coord) ** 2
        """Можно так ещё"""
        ########################################
        if x != y:
            return (x + y) ** 0.5
        else:
            raise Exception('point1 == point2')
        ########################################

    def __str__(self):
        return f'Line {str(self.first_point), str(self.second_point)} with length {self.length()}'


line1 = Line(point1, point2)

""" Задание №2
Напишите декоратор, измеряющий время выполнения функции. Работа функции не должна быть и возвращаемое значение нарушено 
работой декоратора"""


def timer(some_function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        some_function(*args, **kwargs)
        print(f'{(datetime.now() - start).microseconds} MSs required to perform the {some_function}')
        return some_function

    return wrapper


@timer
def fibo_f():
    res = [1, 1]
    for x in range(2, 10000):
        res.append(res[x - 2] + res[x - 1])


@timer
def sumo_f():
    num_list = [x for x in range(1000000) if x % 2 == 0]


fibo_f()
sumo_f()

""" Задание №3
* Модифицируйте декоратор таким образом, чтобы декоратор изменял возвращаемое значение функции на дикт
{
'result': результат работы функции
'time' : время выполнения в формате H-MM-SS-MS (часы-минуты-секунды-милисекунды)
}"""


def timer_2(some_function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        function_data = some_function(*args, **kwargs)
        end = datetime.now()
        time = str(end - start).split(':')
        time[2] = time[2].split('.')
        time = time[0] + 'H' + ' - ' + time[1] + 'M' + ' - ' + time[2][0] + 'S' + ' - ' + time[2][0][0:2] + 'mS'
        res = {'result': function_data,
               'time': time}
        print(res)
        return some_function

    return wrapper


@timer_2
def fibo_f_2():
    res = [1, 1]
    for x in range(2, 200000):  # будет ~4сек.
        res.append(res[x - 2] + res[x - 1])
    return 'Some type of result'


fibo_f_2()
