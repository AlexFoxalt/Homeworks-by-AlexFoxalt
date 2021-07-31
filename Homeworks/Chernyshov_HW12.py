"""Чернышов Алексей HW12"""
from math import sqrt

"""
Напишите класс Triangle. Треугольник должен определяться с помощью обьектов-точек (класс Point). Реализуйте в нем метод,
 который бы возвращал площадь треугольника.
 
 *Реализуйте в классе Triangle возможность итерировать его обьекты по вершинам (точкам)
"""


class Point:
    def __init__(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.x_coord = x
            self.y_coord = y
        else:
            raise TypeError('Not int')

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if (self.x_coord, self.y_coord) == (other.x_coord, other.y_coord):
                return True
            else:
                return False
        else:
            raise Exception('Arg is not a Point type')

    def length(self, arg):
        if isinstance(arg, self.__class__):
            # По формуле Хряпы))
            return (((arg.x_coord - self.x_coord) ** 2) + ((arg.y_coord - self.y_coord) ** 2)) ** 0.5
        else:
            raise Exception('Arg is not a Point type')

class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        if isinstance(a, Point) and isinstance(b, Point) and isinstance(c, Point):
            if a != b and b != c and c != a:
                self.a = a
                self.b = b
                self.c = c
                self.a_b_length = a.length(b)
                self.b_c_length = b.length(c)
                self.c_a_length = c.length(a)
            else:
                raise Exception('Points have same coordinates')
        else:
            raise Exception('Incorrect type of data')

    def area_of_triangle(self):
        # По формуле Герона
        p = (self.a_b_length + self.b_c_length + self.c_a_length) * 0.5
        area = sqrt(p * (p - self.a_b_length) * (p - self.b_c_length) * (p - self.c_a_length))
        print('Area =', round(area, 2))
        return

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        list_of_points = [('a', self.a.x_coord, self.a.y_coord),
                          ('b', self.b.x_coord, self.b.y_coord),
                          ('c', self.c.x_coord, self.c.y_coord)]
        if self._counter >= 3:
            raise StopIteration
        res = list_of_points[self._counter]
        self._counter += 1
        return res


figure1 = Triangle(Point(0, 0), Point(5, 5), Point(0, 5))
# Проверка 'уродцев'
# figure2 = Triangle(('0', '0'), Point(False, True), Point(0, 0))
# figure3 = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))

figure1.area_of_triangle()

for point1 in figure1:
    print('1st', point1)

for point2 in figure1:
    print('2nd', point2)

for point3 in figure1:
    print('3rd', point3)