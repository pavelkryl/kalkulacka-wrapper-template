
from hwmodul import HwModul, BinarniOperace, HwModulImpl
from kalkulacka_kontrakt import AbstractKalkulator


class HwKalkulator(AbstractKalkulator):

    def __init__(self, hw_modul: HwModul):
        self._hw = hw_modul

    def plus(self, op1: int, op2: int) -> int:
        return int(self._hw.binarni(BinarniOperace.PLUS, op1, op2))

    def minus(self, op1: int, op2: int) -> int:
        return int(self._hw.binarni(BinarniOperace.MINUS, op1, op2))

    def multi(self, op1: int, op2: int) -> int:
        return int(self._hw.binarni(BinarniOperace.KRAT, op1, op2))

    def divide(self, op1: int, op2: int) -> float:
        return self._hw.binarni(BinarniOperace.DELENO, op1, op2)



hw_k = HwKalkulator(HwModulImpl())