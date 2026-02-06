class Byte:

    def __init__(self, str_byte=None):
        if str_byte is None:
            self.list = [0, 0, 0, 0, 0, 0, 0, 0]
        elif len(str_byte) == 8 and all(c in '01' for c in str_byte):
            self.list = [int(c) for c in str_byte]
        else:
            raise ValueError("Error creating a Byte")

    def __str__(self):
        result = ""
        for digit in self.list:
            result += str(digit)
        return result

    def to_int(self):
        result = 0
        num = [7, 6, 5, 4, 3, 2, 1, 0]
        for i in range(0, 8):
            result += self.list[i] * (2 ** num[i])
        return result

    def int_to_bit(self, integer):
        integer = integer % 256
        bits2 = [128, 64, 32, 16, 8, 4, 2, 1]
        for i in range(8):
            self.list[i] = integer // (bits2[i])
            integer = integer % bits2[i]

    def __add__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            sum_integers = self.to_int() + other.to_int()
            result.int_to_bit(sum_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __sub__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            sub_integers = self.to_int() - other.to_int()
            if sub_integers < 0:
                raise ValueError("Sub doesnt support negative byte")
            result.int_to_bit(sub_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __mul__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            mul_integers = self.to_int() * other.to_int()
            mul_integers %= 256
            result.int_to_bit(mul_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __floordiv__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            floor_integers = self.to_int() // other.to_int()
            result.int_to_bit(floor_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __div__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            floor_integers = self.to_int() / other.to_int()
            result.int_to_bit(floor_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __mod__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            mood_integers = self.to_int() % other.to_int()
            result.int_to_bit(mood_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __pow__(self, other):
        result = Byte()
        if isinstance(other, Byte):
            pow_integers = self.to_int() ** other.to_int()
            result.int_to_bit(pow_integers)
            return result
        else:
            raise TypeError("Operand must be Byte")

    def __lshift__(self, other):
        if not isinstance(other, int):
            print(f"Cannot lshift {other} is not Integer")
            return None
        if other in range(0, 8):
            new_list = self.list[other:8]
            for x in range(other):
                new_list.append(0)
            return new_list
        elif other >= 8:

            return [0, 0, 0, 0, 0, 0, 0, 0]
        else:
            raise TypeError(f"Cannot lshift {other} is lower than 0")

    def __rshift__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Cannot lshift {other} is not Integer")
        if other in range(0, 8):
            new_list = self.list[0:8 - other]
            for x in range(other):
                new_list.insert(0, 0)
            return new_list
        elif other >= 8:
            return [0, 0, 0, 0, 0, 0, 0, 0]
        else:
            raise TypeError(f"Cannot rshift {other} is lower than 0")

    def __and__(self, other):
        if isinstance(other, Byte):
            return [int(bool(self.list[index]) and bool(other.list[index])) for index in range(8)]
        else:
            raise TypeError(f"There is not in the same Class{other} and {self}")

    def __or__(self, other):
        if isinstance(other, Byte):
            return [int(bool(self.list[index]) or bool(other.list[index])) for index in range(8)]
        else:
            raise TypeError(f"There is not in the same Class{other} and {self}")

    def __xor__(self, other):
        if isinstance(other, Byte):
            new_byte = Byte()
            new_byte.list = [int((bool(self.list[index]) and not bool(other.list[index])) or (
                    not bool(self.list[index]) and bool(other.list[index]))) for index in range(8)]
            return new_byte
        else:
            raise TypeError(f"There is not in the same Class{other} and {self}")


byte1 = Byte("00000011")
byte2 = Byte("00000101")
print(byte1.to_int())
print(byte2.to_int())
print((byte2 ** byte1).to_int())
