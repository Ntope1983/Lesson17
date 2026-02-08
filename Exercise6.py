class Counter:
    def __init__(self, count=0):
        self.count = count

    def __str__(self):
        return str(self.count)

    def __pos__(self):
        self.count += 1

    def __neg__(self):
        self.count += -1

a=Counter()
for i in range(100):

    print(a)
    +a