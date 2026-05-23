from jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, uticel, jegyar, repulesi_ido):
        super().__init__(jaratszam, uticel, jegyar)
        self._repulesi_ido = repulesi_ido

    # A belföldi járat repülési idejének lekérdezése
    @property
    def repulesi_ido(self):
        return self._repulesi_ido
    
    # Belföldi járatok alapáron foglalhatók
    def get_ar(self) -> float:
        return self.jegyar