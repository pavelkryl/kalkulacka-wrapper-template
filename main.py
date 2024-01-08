from kalkulator import Kalkulator
from abstract_kalkulator import AbstractKalkulator


# test pouziti:
k : AbstractKalkulator = Kalkulator()

# toto nemente
r = k.plus(2,3)
print(f"2 plus 3 je {r}")