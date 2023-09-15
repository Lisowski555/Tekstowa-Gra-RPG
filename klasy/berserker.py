from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik


class Berserker(Klasa):
    def __init__(self):
        super().__init__(zycie=3, sila=3, inteligencja=-2, zwinnosc=-2, pasywna=True)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        if gracz.zycie < gracz.calkowite_zycie / 2:
            gracz.sila += 1
            print(f"Moja sila rosnie! Aktualnie wynosi: {gracz.sila}")
