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


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        if isinstance(a, Point) and isinstance(b, Point) and isinstance(c, Point):
            if (a.x_coord, a.y_coord) != (b.x_coord, b.y_coord) and \
                    (b.x_coord, b.y_coord) != (c.x_coord, c.y_coord) and \
                    (c.x_coord, c.y_coord) != (a.x_coord, a.y_coord):
                self.a = a
                self.b = b
                self.c = c
                # По формуле Хряпы))
                self.a_b_length = (((b.x_coord - a.x_coord) ** 2) + ((b.y_coord - a.y_coord) ** 2)) ** 0.5
                self.b_c_length = (((c.x_coord - b.x_coord) ** 2) + ((c.y_coord - b.y_coord) ** 2)) ** 0.5
                self.c_a_length = (((a.x_coord - c.x_coord) ** 2) + ((a.y_coord - c.y_coord) ** 2)) ** 0.5
            else:
                raise Exception('Points have same coordinates')
        else:
            raise Exception('Incorrect type of data')

    def area_of_triangle(self):
        """По формуле Герона"""
        p = (self.a_b_length + self.b_c_length + self.c_a_length) * 0.5
        area = sqrt(p * (p - self.a_b_length) * (p - self.b_c_length) * (p - self.c_a_length))
        print(round(area, 2))
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


figure1 = Triangle(Point(0, 1), Point(2, 5), Point(0, 5))
# figure2 = Triangle(Point('0', '0'), Point(False, True), Point(0, 0))
# figure3 = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))

figure1.area_of_triangle()
for x in figure1:
    print(x)
