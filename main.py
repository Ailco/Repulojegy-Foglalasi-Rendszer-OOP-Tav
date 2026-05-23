from datetime import datetime
from legi_tarsasag import LegiTarsasag
from belfoldi_jarat import BelfoldiJarat
from nemzetkozi_jarat import NemzetkoziJarat
from jegy_foglalas import JegyFoglalas
from foglalasi_rendszer import FoglalasiRendszer

def main():
    wizz_air = LegiTarsasag("Wizz Air")

    j1 = BelfoldiJarat("W6 2352", "Kaposvár", 5000, 35)
    j2 = NemzetkoziJarat("W6 2368", "Párizs", 20000, 145)
    j3 = NemzetkoziJarat("W6 2394", "Lisszabon", 15000, 180)

    wizz_air.jarat_hozzaadasa(j1)
    wizz_air.jarat_hozzaadasa(j2)
    wizz_air.jarat_hozzaadasa(j3)

    rendszer = FoglalasiRendszer(wizz_air)
    
    rendszer.alap_foglalas_hozzaadasa(JegyFoglalas(j1, "Kovács Luca", datetime(2026, 7, 20)))
    rendszer.alap_foglalas_hozzaadasa(JegyFoglalas(j1, "Varga Anna", datetime(2026, 7, 21)))
    rendszer.alap_foglalas_hozzaadasa(JegyFoglalas(j2, "Nagy Lili", datetime(2026, 8, 5)))
    rendszer.alap_foglalas_hozzaadasa(JegyFoglalas(j2, "Takács Barbara", datetime(2026, 8, 6)))
    rendszer.alap_foglalas_hozzaadasa(JegyFoglalas(j3, "Horváth Bence", datetime(2026, 9, 10)))
    rendszer.alap_foglalas_hozzaadasa(JegyFoglalas(j3, "Kiss Dávid", datetime(2026, 9, 11)))

    while True:
        print("\n=== REPÜLŐJEGY FOGLALÁSI RENDSZER ===")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        
        valasztas = input("Válassz egy menüpontot (1-4): ")

        if valasztas == "1":
            rendszer.jaratok_listazasa()
            jaratszam = input("Kérem a foglalni kívánt járat számát: ")
            utas_nev = input("Kérem az utas nevét: ")
            datum_str = input("Kérem a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            
            try:
                fizetendo = rendszer.jegy_foglalasa(jaratszam, utas_nev, datum_str)
                print(f"\nSikeres foglalás! Fizetendő összeg: {fizetendo:.0f} HUF.")
            except ValueError as e:
                print(f"\nHiba történt a foglalás során: {e}")
        
        elif valasztas == "2":
            rendszer.foglalasok_listazasa()
            utas_nev = input("Kérem a lemondani kívánt foglalás utasának nevét: ")
            jaratszam = input("Kérem a járatszámot: ")
            datum_str = input("Kérem a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            
            try:
                if rendszer.foglalas_lemondasa(utas_nev, jaratszam, datum_str):
                    print(f"\nA(z) {utas_nev} nevű utas {jaratszam} számú járatra szóló foglalása sikeresen törölve.")
            except ValueError as e:
                print(f"\nHiba történt a lemondás során: {e}")
        
        elif valasztas == "3":
            rendszer.foglalasok_listazasa()
        
        elif valasztas == "4":
            print("\nKilépés a programból.")
            break
        
        else:
            print("\nÉrvénytelen választás! Kérlek az 1-4 közötti számok közül válassz.")

if __name__ == "__main__":
    main()