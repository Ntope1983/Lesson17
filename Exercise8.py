# This Byte class correctly models an 8-bit sequence
# with proper input validation, string representation,
# and supports indexing and iteration via __getitem__.
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

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return 8


def __setitem__(self, pos, value):
    if not (0 <= pos < 8):
        raise IndexError("Index must be 0–7 for Byte")
    if value not in (0, 1):
        raise ValueError("Byte can only hold 0 or 1")
    self.list[pos] = value


byte = Byte("01011010")
for bit in byte:
    print(bit)
