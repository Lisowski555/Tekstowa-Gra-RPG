from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik


class Alkoholik(Klasa):
    def __init__(self):
        super().__init__(zycie=1, zwinnosc=-1, inteligencja=9, charyzma=5, pasywna=True)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        gracz.charyzma += 5
        print(f"Ta *HYK* studnia nie ma dna...Moja charyzma wynosi teraz*HYK*: {gracz.charyzma}")
