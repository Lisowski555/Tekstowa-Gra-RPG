from przeciwnicy.przeciwnik import Przeciwnik


class Ksiezniczka(Przeciwnik):
    def __init__(self):
        super().__init__(zycie=5, sila=4, zwinnosc=5, zbroja=2, charyzma=15, inteligencja=10)

    def __str__(self):
        return "Ksiezniczka"
