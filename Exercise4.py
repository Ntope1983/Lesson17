class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, + self.z + other.z)
        else:
            raise TypeError(f"{other} must be Point instance")

    def __iadd__(self, other):
        if isinstance(other, Point3D):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        else:
            raise TypeError(f"{other} must be Point instance")


a = Point3D(1, 1, 1, )
b = Point3D(2, 2, 2)
print(a + b)
c = a + b
print(c)
a = a + b
print(a)
a += b
print(a)
