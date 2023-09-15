from przeciwnicy.przeciwnik import Przeciwnik


class LisKosmita(Przeciwnik):
    def __init__(self):
        super().__init__(zycie=15, sila=20, zwinnosc=17, zbroja=10, charyzma=21, inteligencja=13)

    def __str__(self):
        return "LisKosmita"
