class Length:
    def __init__(self, value, unit):
        self.values = {}

        if unit == "m":
            self.values['m'] = value
            self.values['cm'] = value * 100
            self.values['in'] = value * 39.37

        elif unit == "cm":
            self.values['m'] = value / 100
            self.values['cm'] = value
            self.values['in'] = value / 2.54  # ← fixed

        elif unit == "in":
            self.values['m'] = value / 39.37
            self.values['cm'] = value * 2.54
            self.values['in'] = value

        else:
            raise ValueError("Error in unit. must be m, cm or in")

    def __str__(self):
        return str(round(self.values["m"], 2)) + " m"

    def __add__(self, other):
        if isinstance(other, Length):
            sum2 = self.values['m'] + other.values['m']
            return Length(sum2, 'm')
        else:
            raise TypeError(f"{other} must be Length instance")

    def __round__(self, digits=None):
        return Length(round(self.values['m'], digits), "m")

    def __int__(self):
        return Length(int(self.values['m']), "m")


x = Length(2.54, "cm")  # → 1 inch
y = Length(1, "in")  # → 2.54 cm
z = Length(1.9513, "m")  # → 100 cm → 39.37 in
print(z.__int__())
