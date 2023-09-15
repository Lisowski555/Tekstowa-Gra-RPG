from przeciwnicy.przeciwnik import Przeciwnik


class Wilk(Przeciwnik):
    def __init__(self):
        super().__init__(zycie=10, sila=6, zwinnosc=14, zbroja=4, charyzma=15, inteligencja=7)

    def __str__(self):
        return "Wilk"
