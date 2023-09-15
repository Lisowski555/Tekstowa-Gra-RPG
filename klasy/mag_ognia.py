from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik
from mechaniki.kostka import d20


class MagOgnia(Klasa):
    def __init__(self):
        super().__init__(zycie=-1, zwinnosc=-2, inteligencja=4, charyzma=2, zbroja=2)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        przeciwnik.zycie -= d20()
        print(f"Po ataku kula ognia przeciwnik ma tyle zycia: {przeciwnik.zycie}")
