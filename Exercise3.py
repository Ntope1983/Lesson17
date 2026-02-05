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


    def __add__(self, other):
        if isinstance(other, Byte):
            print(other)

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
            print(f"Cannot lshift {other} is lower than 0")
            return None

    def __rshift__(self, other):
        if not isinstance(other, int):
            print(f"Cannot lshift {other} is not Integer")
            return None
        if other in range(0, 8):
            new_list = self.list[0:8 - other]
            for x in range(other):
                new_list.insert(0, 0)
            return new_list
        elif other >= 8:
            return [0, 0, 0, 0, 0, 0, 0, 0]
        else:
            print(f"Cannot rshift {other} is lower than 0")
            return None

    def __and__(self, other):
        if isinstance(other, Byte):
            return [int(bool(self.list[index]) and bool(other.list[index])) for index in range(8)]
        else:
            print(f"There is not in the same Class{other} and {self}")
            return None

    def __or__(self, other):
        if isinstance(other, Byte):
            return [int(bool(self.list[index]) or bool(other.list[index])) for index in range(8)]
        else:
            print(f"There is not in the same Class{other} and {self}")
            return None

    def __xor__(self, other):
        if isinstance(other, Byte):
            new_byte = Byte()
            new_byte.list = [int((bool(self.list[index]) and not bool(other.list[index])) or (
                    not bool(self.list[index]) and bool(other.list[index]))) for index in range(8)]
            return new_byte
        else:
            print(f"There is not in the same Class{other} and {self}")
            return None


byte1 = Byte("01111011")
byte2 = Byte("01010001")
print(byte1 + byte2)
