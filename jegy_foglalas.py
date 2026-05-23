class JegyFoglalas:
    def __init__(self, jarat, utas_nev, datum):
        if not utas_nev.strip():
            raise ValueError("Az utas neve nem lehet üres.")
        if datum is None:
            raise ValueError("A dátum megadása kötelező.")
        self._jarat = jarat
        self._utas_nev = utas_nev
        self._datum = datum

    @property
    def jarat(self):
        return self._jarat

    @property
    def utas_nev(self):
        return self._utas_nev
    
    @property
    def datum(self):
        return self._datum

    def foglalas_info(self):
        return f"Utas: {self._utas_nev}, Járatszám: {self._jarat.jaratszam}, Célállomás: {self._jarat.uticel}, Dátum: {self._datum.strftime('%Y-%m-%d')}"

    def __str__(self):
        return self.foglalas_info()

    def jegyar(self):
        return self._jarat.get_ar()