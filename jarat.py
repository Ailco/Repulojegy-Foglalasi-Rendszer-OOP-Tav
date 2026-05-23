from abc import ABC, abstractmethod


class Jarat(ABC):
    def __init__(self, jaratszam: str, uticel: str, jegyar: int):
        if not jaratszam.strip():
            raise ValueError("A járatszám nem lehet üres.")

        if not uticel.strip():
            raise ValueError("Az úti cél nem lehet üres.")

        if jegyar <= 0:
            raise ValueError("A jegyárnak pozitívnak kell lennie.")

        self._jaratszam = jaratszam
        self._uticel = uticel
        self._jegyar = jegyar

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def uticel(self):
        return self._uticel

    @property
    def jegyar(self):
        return self._jegyar

    @abstractmethod
    def get_ar(self) -> float:
        pass
    
    def __str__(self):
        return f"{self._jaratszam} - {self._uticel}"