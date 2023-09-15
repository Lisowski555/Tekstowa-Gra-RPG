from gracz import Gracz
from przeciwnicy.przeciwnik import Przeciwnik
from mechaniki.kostka import *
from przeciwnicy.lis_kosmita import LisKosmita


class Walka:
    def __init__(self, gracz: Gracz, wrog: Przeciwnik):
        self.gracz = gracz
        self.wrog = wrog

    def atakuje(self, kto: Gracz or Przeciwnik):
        return d20() + modyfikator(kto.najlepszy_atak())

    def obraniam(self, kto: Przeciwnik or Gracz):
        rand = random.randint(1, 11)
        unik = modyfikator(kto.zwinnosc)
        if rand > unik:
            return kto.zbroja
        else:
            return 1000

    def obrazenia(self, sila):
        return int(sila / 2 + d4())

    def tura(self):
        print("\nNowa tura\n")
        if self.gracz.klasa.pasywna:
            self.gracz.klasa.umiejetnosc(self.gracz, self.wrog)
        atak = self.atakuje(self.gracz)
        obrona = self.obraniam(self.wrog)
        if atak > obrona:
            obrazenia = self.obrazenia(max(self.gracz.sila, self.gracz.inteligencja))
            self.wrog.zycie -= obrazenia
            print(f"\tTrafilem i zadalem {obrazenia} obrazen!")
        else:
            print("\tWrog obronil sie przed ciosem.")

        atak = self.atakuje(self.wrog)
        obrona = self.obraniam(self.gracz)
        if atak > obrona:
            obrazenia = self.obrazenia(max(self.wrog.sila, self.wrog.inteligencja))
            self.gracz.zycie -= obrazenia
            print(f"\tZostalem trafiony i otrzymalem {obrazenia} obrazen!")
        else:
            print("\tObronilem sie przed ciosem.")

    def wykonaj(self):
        while self.gracz.zycie > 0 and self.wrog.zycie > 0:
            self.tura()
            print(f"\t\tGracz:{self.gracz.zycie}\tWrog:{self.wrog.zycie}")
        if self.gracz.zycie > 0:
            print("\t\tWygralem!")
            return
        else:
            print("Przegralem...\n\t\t\tGAME OVER")
            exit(0)

    def oberwij(self):
        atak = self.atakuje(self.wrog)
        obrona = self.obraniam(self.gracz)
        if atak > obrona:
            obrazenia = self.obrazenia(max(self.wrog.sila, self.wrog.inteligencja))
            self.gracz.zycie -= obrazenia
            print(f"\tZostalem trafiony i otrzymalem {obrazenia} obrazen!\nMoje zycie wynosi teraz: {self.gracz.zycie}")
            if self.gracz.zycie <= 0:
                print("Przegrales...\n\t\t\tGAME OVER")
                exit(0)
        else:
            print("\tObronilem sie przed ciosem.")