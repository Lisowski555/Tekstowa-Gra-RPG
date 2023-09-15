from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik
from mechaniki.kostka import *


class Wojownik(Klasa):
    def __init__(self):
        super().__init__(zycie=3, zwinnosc=1, inteligencja=-3, sila=3, pasywna=True)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        if d4() > 2:
            gracz.zycie += 2
            print(f"Aaaaaa! W wirze walki czuje jak wracaja mi sily witalne, a ich aktualna wartosc to: {gracz.zycie}")
