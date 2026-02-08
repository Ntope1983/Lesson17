class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Wrong index in Point3D.Must be 0:x,1:y,2:z")

    def __len__(self):
        return 3

    def __setitem__(self, pos, value):
        if pos == 0:
            self.x=value
        elif pos == 1:
            self.y=value
        elif pos == 2:
            self.z=value
        else:
            raise IndexError("Wrong pos in Point3D.Must be 0:x,1:y,2:z")



