from jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, uticel, jegyar, repulesi_ido):
        super().__init__(jaratszam, uticel, jegyar)
        self._repulesi_ido = repulesi_ido

    @property
    def repulesi_ido(self):
        return self._repulesi_ido
    
    def get_ar(self) -> float:
        return self.jegyar