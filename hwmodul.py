from abc import ABC, abstractmethod
from enum import Enum


class BinarniOperace(Enum):
    PLUS = 0
    MINUS = 1
    KRAT = 2
    DELENO = 3
    

class UnarniOperace(Enum):
    SIN = 0
    COS = 1
    TG = 2
    COTG = 3
    


class HwModul(ABC):

    @abstractmethod
    def binarni(self, operace: BinarniOperace, operand1: float, operand2: float) -> float:
        ...

    @abstractmethod
    def unarni(self, operace: UnarniOperace, operand: float) -> float:
        ...

class HwModulImpl(HwModul):

    def binarni(self, operace: BinarniOperace, operand1: float, operand2: float) -> float:
        return 0

    def unarni(self, operace: UnarniOperace, operand: float) -> float:
        return 0