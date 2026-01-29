# Using __str__ to print nicely and __eq__ to compare objects
from functools import total_ordering
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def print_x_y(self):
        print(f"({self.x},{self.y})")


@total_ordering
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
        return "Line with PointA:" + str(self.point_a) + " and PointB:" + str(self.point_b)

    def set_point_a(self, point):
        self.point_a = point

    def set_point_b(self, point):
        self.point_b = point

    def length(self):
        return sqrt((self.point_a.x - self.point_b.x) ** 2 + (self.point_a.y - self.point_b.y) ** 2)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.length() == other
        return self.length() == other.length()

    def __lt__(self, other):
        if isinstance(other, int):
            return self.length() < other
        return self.length() < other.length()


line_1 = Line(Point(0, 0), Point(3, 4))
line_2 = Line(Point(2, 2), Point(10, 10))
if line_1 <= 5:
    print(f"{line_1.length()} is equal than {2}")
