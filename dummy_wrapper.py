
from abstract_kalkulator import AbstractKalkulator


class DummyWrapper(AbstractKalkulator):

    def __init__(self, delegate: AbstractKalkulator) -> None:
        self._delegate = delegate

    def plus(self, op1: int, op2: int) -> int:
        return self._delegate.plus(op1, op2)

    def minus(self, op1: int, op2: int) -> int:
        return self._delegate.minus(op1, op2)

    def multi(self, op1: int, op2: int) -> int:
        return self._delegate.multi(op1, op2)

    def divide(self, op1: int, op2: int) -> float:
        return self._delegate.divide(op1, op2)
