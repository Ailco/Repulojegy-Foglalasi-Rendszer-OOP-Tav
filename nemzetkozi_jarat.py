from jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, uticel, jegyar, repulesi_ido):
        super().__init__(jaratszam, uticel, jegyar)
        self._repulesi_ido = repulesi_ido
    
    # A nemzetközi járat repülési idejének lekérdezése
    @property
    def repulesi_ido(self):
        return self._repulesi_ido

    # Nemzetközi járatok esetén 50% felár kerül a jegyárra
    def get_ar(self) -> float:
        return self.jegyar * 1.5