# Naprogramujte wrapper

# Krok 1.

Naprogramujte wrapper, který bude:

- implementovat: `AbstraktKalkulator`
- v konstruktoru brát argument typu `AbstraktKalkulator`, který uloží do fieldu/pole `self._kalkulator`
- musíte implementovat všechny metody `AbstraktKalkulator`:
  - jednoduše se jen provolejte skrz `self._kalkulator` na skutečnou implementaci
- úpravou v main.py ověřte že to funguje, kulkulačku koonstruujte takto:

```
kalkulator : AbstractKalkulator = KalkulatorWrapper(Kalkulator())
```

## Krok 2.

Naprogramujte tři různé wrappery.

### Wrapper 1. - logování
- nejjednodušší
- jenom pomocí print vypiště co se provádí za operaci
- následně delegujte na delegáta
- před vrácením výsledku vypište jaký je výsledek

### Wrapper 2. - historie operací
- složitější
- v tomto wrapperu budete potřebovat držet historii prováděných operací (nejlépe jako seznam)
- při každé zavolené operaci si uložíte:
  - jaká operace byla volaná
  - jaké byly operandy
  - jaký byl vrácený výsledek
- uděláte navíc metodu, která vám vrátí uloženou historii operací

### Wrapper 2. - historie operací
- nejsložitější
- 
