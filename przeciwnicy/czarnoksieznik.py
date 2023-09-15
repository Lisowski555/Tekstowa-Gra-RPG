from przeciwnicy.przeciwnik import Przeciwnik


class Czarnoksieznik(Przeciwnik):
    def __init__(self):
        super().__init__(zycie=101, sila=10, zwinnosc=0, zbroja=30, charyzma=25, inteligencja=30)

    def __str__(self):
        return "Czarnoksieznik"
