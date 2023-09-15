from klasy.klasa import Klasa
from przeciwnicy.przeciwnik import Przeciwnik
from mechaniki.akcje.walka import Walka


class Asasyn(Klasa):
    def __init__(self):
        super().__init__(zycie=1, zwinnosc=3, inteligencja=2, charyzma=-1)

    def umiejetnosc(self, gracz, przeciwnik: Przeciwnik):
        walka = Walka(gracz, przeciwnik)
        obrazenia = walka.obrazenia(gracz.zwinnosc)
        przeciwnik.zycie -= obrazenia
        print(f"Wbilem sztylet w plecy i zadalem {obrazenia} obrazen")
