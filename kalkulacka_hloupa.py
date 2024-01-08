
from kalkulacka_kontrakt import AbstractKalkulator


class HloupyKalkulator(AbstractKalkulator):

    def plus(self, op1: int, op2: int) -> int:
        return op1 + op2

    def minus(self, op1: int, op2: int) -> int:
        return op1 - op2

    def multi(self, op1: int, op2: int) -> int:
        acc = 0
        for i in range(op2):
            acc +=op1
        return acc

    def divide(self, op1: int, op2: int) -> float:
        res = op1
        acc = 0
        while res > 0:
            res -= op2
            acc += 1
        return acc



k = HloupyKalkulator()
print(k.multi(4,5))
print(k.divide(10,4))