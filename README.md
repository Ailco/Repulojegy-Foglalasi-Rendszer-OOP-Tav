# Repülőjegy Foglalási Rendszer

Egyszerű konzolos Python alkalmazás repülőjegyek foglalására, lemondására és az aktív foglalások listázására.

## Funkciók

- elérhető járatok listázása
- jegyfoglalás név, járatszám és dátum alapján
- foglalás lemondása
- aktív foglalások megtekintése
- hibás adatok kezelése
- múltbeli dátum tiltása

## Osztályok

- `Jarat`: absztrakt ősosztály
- `BelfoldiJarat`: belföldi járatok kezelése
- `NemzetkoziJarat`: nemzetközi járatok kezelése
- `LegiTarsasag`: járatok tárolása
- `JegyFoglalas`: egy foglalás adatai
- `FoglalasiRendszer`: foglalási műveletek kezelése

## Előre betöltött adatok

A program induláskor tartalmaz:

- 1 légitársaságot
- 3 járatot
- 6 előre létrehozott foglalást

## Futtatás

```bash
python main.py
```