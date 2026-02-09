#Clean, functional Queue class with
# proper operator overloading for +, +=, -, and len.
class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, element):
        self.array.append(element)

    def dequeue(self):
        if self.array:
            return self.array.pop(0)
        else:
            return None

    def __str__(self):
        result = [str(element) for element in self.array]
        return ",".join(result)

    def __add__(self, other):
        result = Queue()
        result.array = self.array.copy()
        result.enqueue(other)
        return result

    def __iadd__(self, other):
        self.enqueue(other)
        return self

    def __neg__(self):
        self.dequeue()
        return self

    def __len__(self):
        return len(self.array)


q = Queue()
q.enqueue([1, 2, 3])
q.enqueue("liza")
q.enqueue((1, 2, 3, 4))
q.enqueue({1, 2, 3, 44, 5, 5})
print(q)
q += "last que"
print(q)
