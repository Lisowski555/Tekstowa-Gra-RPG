from przeciwnicy.przeciwnik import Przeciwnik


class Niedzwiedz(Przeciwnik):
    def __init__(self):
        super().__init__(zycie=30, sila=15, zwinnosc=6, zbroja=15, charyzma=15, inteligencja=7)

    def __str__(self):
        return "Niedwiedz"
