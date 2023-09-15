from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik
from mechaniki.kostka import *


class Paladyn(Klasa):
    def __init__(self):
        super().__init__(zycie=2, sila=3, inteligencja=-2, zwinnosc=-1, charyzma=2)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        gracz.zbroja += d6()
        print(f"Ale mam fajna diaxowa zbrojke z ostatniej swiatyni na ta potyczke! Jej pancerz to az: {gracz.zbroja}!")
