from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik


class Nekromanta(Klasa):
    def __init__(self):
        super().__init__(zycie=3, inteligencja=4, charyzma=-3, zbroja=-1, zwinnosc=-2)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        gracz.zycie += 15
        print(f"Razem z moim nieumarlym posiadajacym {15} zycia mamy {gracz.zycie} zycia muhahaha!")
