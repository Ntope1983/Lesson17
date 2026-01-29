# # Distance Between Two Points Using OOP
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_x_y(self):
        print(f"({self.x},{self.y})")


class Line:
    def __init__(self, point_a=None, point_b=None):
        if point_a is None:
            self.point_a = Point(0, 0)
        else:
            self.point_a = point_a
        if point_b is None:
            self.point_b = Point(0, 0)
        else:
            self.point_b = point_b

    def __str__(self):
        print(f"{self.point_a.print_x_y()}")





    def set_point_a(self, point):
        self.point_a = point

    def set_point_b(self, point):
        self.point_b = point

    def length(self):
        print(sqrt((self.point_a.x - self.point_b.x) ** 2 + (self.point_a.y - self.point_b.y) ** 2))

line_1=Line(Point(2,2),Point(3,3))
print(line_1)