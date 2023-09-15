import copy


class Przeciwnik:
    def __init__(self, zycie=0, sila=0, zwinnosc=0, inteligencja=0, zbroja=0, charyzma=0):
        self.zycie: int = zycie
        self.sila: int = sila
        self.zwinnosc: int = zwinnosc
        self.inteligencja: int = inteligencja
        self.zbroja: int = zbroja
        self.charyzma: int = charyzma

    def najlepszy_atak(self):
        return max(self.sila, self.zwinnosc)

    def klonuj(self):
        klon = copy.deepcopy(self)
        return klon
