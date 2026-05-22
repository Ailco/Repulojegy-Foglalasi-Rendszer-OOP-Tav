from jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, uticel, jegyar):
        super().__init__(jaratszam, uticel, jegyar)

    def get_ar(self) -> float:
        return self.jegyar * 1.2