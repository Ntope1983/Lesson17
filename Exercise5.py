# special method ~ __invert_
# _(self):
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

    def __invert__(self):
        result = Byte()
        result.list = self.list.copy()
        for index in range(len(result.list)):
            if result.list[index] == 0:
                result.list[index] = 1
            else:
                result.list[index] = 0
        return result


byte1 = Byte("11100011")
print(~byte1)
