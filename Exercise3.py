
class Byte:

    def __init__(self,str_byte=None):
        if str_byte is None:
            self.list = [0, 0, 0, 0, 0, 0, 0, 0]
        elif len(str_byte) == 8 and all(c in '01' for c in str_byte):
            self.list=[int(c) for c in str_byte]
        else:
            raise ValueError("Error creating a Byte")

    def __str__(self):
        result=""
        for digit in self.list:
            result+=str(digit)
        return result

    def __lshift__(self,other):
        if not isinstance(other,int):
            print(f"Cannot lshift {other} is not Integer")
            return None
        if other in range(0,8):
            new_list=self.list[other:8]
            for x in range(other):
                new_list.append(0)
            return new_list
        else:
            print("not Ok")

byte=Byte("11111111")
byte<<2
