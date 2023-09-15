from przeciwnicy.przeciwnik import Przeciwnik


class Klasa:

    def __init__(self, zycie=0, sila=0, zwinnosc=0, inteligencja=0, charyzma=0, zbroja=0, pasywna=False):
        self.zycie: int = zycie
        self.sila: int = sila
        self.zwinnosc: int = zwinnosc
        self.inteligencja: int = inteligencja
        self.charyzma: int = charyzma
        self.zbroja: int = zbroja
        self.pasywna: bool = pasywna

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        pass
