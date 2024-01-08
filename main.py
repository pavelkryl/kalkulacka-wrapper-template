from kalkulator import Kalkulator
from abstract_kalkulator import AbstractKalkulator


# test pouziti:
kalkulator : AbstractKalkulator = Kalkulator()

# zde zavolejte více než jen jednu operaci, abyste ověřili funkčnost
r = kalkulator.plus(2,3)
print(f"2 plus 3 je {r}")