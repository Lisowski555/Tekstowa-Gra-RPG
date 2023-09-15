from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik
from mechaniki.kostka import d4


class Lowca(Klasa):
    def __init__(self):
        super().__init__(zycie=3, zwinnosc=1, inteligencja=1, charyzma=2, zbroja=1, pasywna=True)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        gracz.zwinnosc += d4()
        print(f"Moja zwinnosc wynosi w tym momencie: {gracz.zwinnosc}")
