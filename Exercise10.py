import math


class Cycle:
    def __init__(self, c):
        self.c = c

    def __str__(self):
        return str(f"x² + y² = {self.c}")

    def __eq__(self, other):
        return self.c == other.c

    def __lt__(self, other):
        if isinstance(other, Cycle):
            return self.c < other.c
        elif isinstance(other, float) or isinstance(other, int):
            return self.c < other
        else:
            raise ValueError(f"{other} must be number or instance of Cycle")

    def __call__(self, *x):
        if len(x) == 1 and isinstance(x[0], (int, float)):
            if self.c - x[0] ** 2 >= 0:
                y_plus = math.sqrt(self.c - x[0] ** 2)
                y_minus = -math.sqrt(self.c - x[0] ** 2)
                return (x[0], y_minus), (x[0], y_plus)
            else:
                raise ValueError(f"Δεν υπάρχει πραγματική λύση για x={x[0]}")
        elif len(x) == 2:
            d_squared = x[0] ** 2 + x[1] ** 2
            if math.isclose(d_squared, self.c):
                print(f"Το σημείο {x} βρίσκεται πάνω στον κύκλο {self}")
            elif d_squared < self.c:
                print(f"Το σημείο {x} βρίσκεται μέσα στον κύκλο {self}")
            else:
                print(f"Το σημείο {x} βρίσκεται έξω από τον κύκλο {self}")
            return None
        else:
            raise ValueError(f"Το όρισμα {x} πρέπει να έχει 1 ή 2 τιμές")


c1 = Cycle(5)
print(c1(3,2))
print(c1(5,7))
print(c1(7,7))
