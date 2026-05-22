from datetime import datetime
from belfoldi_jarat import BelfoldiJarat
from jegy_foglalas import JegyFoglalas

class FoglalasiRendszer:
    def __init__(self, legitarsasag):
        self._legitarsasag = legitarsasag
        self._foglalasok = []

    def alap_foglalas_hozzaadasa(self, foglalas):
        self._foglalasok.append(foglalas)
    
    def jaratok_listazasa(self):
        print(f"\n--- {self._legitarsasag.nev} Elérhető Járatok ---")
        for jarat in self._legitarsasag.jaratok:
            tipus = "Belföldi" if isinstance(jarat, BelfoldiJarat) else "Nemzetközi"
            print(f"[{tipus}] Járatszám: {jarat.jaratszam} | Uticél: {jarat.uticel} | Ár: {jarat.get_ar():.0f} HUF")
        print("-----------------------------------")

    def jegy_foglalasa(self, jaratszam, utas_nev, datum_str):
        if not utas_nev.strip():
            raise ValueError("Az utas neve nem lehet üres.")
        try:
            foglalas_ideje = datetime.strptime(datum_str, "%Y-%m-%d")
            if foglalas_ideje.date() < datetime.now().date():
                raise ValueError("A foglalás időpontja nem lehet a múltban!")
        except ValueError as e:
            if "does not match format" in str(e):
                raise ValueError("Hibás dátumformátum! Használd az ÉÉÉÉ-HH-NN formátumot.")
            else:
                raise e

        kivalasztott_jarat = None
        for jarat in self._legitarsasag.jaratok:
            if jarat.jaratszam == jaratszam:
                kivalasztott_jarat = jarat
        for foglalas in self._foglalasok:
            if (foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam and foglalas.datum.date() == foglalas_ideje.date()):
                raise ValueError("Erre a járatra ezen a napon már van ilyen néven foglalás.")
        
        if not kivalasztott_jarat:
            raise ValueError("Nem található ilyen járatszám a rendszerben!")

        uj_foglalas = JegyFoglalas(kivalasztott_jarat, utas_nev, foglalas_ideje)
        self._foglalasok.append(uj_foglalas)
        return kivalasztott_jarat.get_ar()

    def foglalas_lemondasa(self, utas_nev, jaratszam):
        for foglalas in self._foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self._foglalasok.remove(foglalas)
                return True
        raise ValueError("Nem található a megadott adatokhoz tartozó aktív foglalás.")

    def foglalasok_listazasa(self):
        print("\n--- Aktív Foglalások ---")
        if not self._foglalasok:
            print("Jelenleg nincsenek aktív foglalások a rendszerben.")
        else:
            for i, foglalas in enumerate(self._foglalasok, 1):
                print(f"{i}. Utas: {foglalas.utas_nev} | Járatszám: {foglalas.jarat.jaratszam} | Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")
        print("------------------------")