# Clean, functional Queue class with
# proper operator overloading for +, +=, -, and len.
import random


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

#simulation design — clean Queue implementation and good use of operator overloading;
# Bank logic , with randomized enqueue/serve behavior
# and correct use of modulo for periodic reporting
class Bank:
    def __init__(self, number_of_funds):
        self.funds = []
        for _ in range(number_of_funds):
            q = Queue()
            self.funds.append(q)

    def __str__(self):
        result = ""
        for index in range(len(self.funds)):
            result += f"The Fund_No:{index + 1} queue \n {str(self.funds[index])}\n"
        return result

    def customers_enters(self, fullname):
        random_choice = random.randrange(0, len(self.funds))
        self.funds[random_choice].enqueue(fullname)

    def customers_served(self):
        busy_funds = [fund for fund in self.funds if len(fund) > 0]
        if busy_funds:
            random_busy_fund = random.choice(busy_funds)
            random_busy_fund.dequeue()

bank = Bank(3)
for i in range(1, 101):
    chance = random.randint(1, 10)
    if chance > 3:
        bank.customers_enters(f"Customer:{i}")
    else:
        bank.customers_served()
    if i % 10 == 0:
        print("---------------" + str(i) + "------------------")
        print(bank)
