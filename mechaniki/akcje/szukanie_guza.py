import walidacja
from mechaniki.akcje.akcja import Akcja
from gracz import Gracz
import random
from mechaniki.kostka import *
from mechaniki.akcje.perswazja import Perswazja
from mechaniki.akcje.ucieczka import Ucieczka
from mechaniki.akcje.walka import Walka


class SzukajGuza(Akcja):
    def __init__(self):
        super().__init__("Szukaj guza")

    def wykonaj(self, gracz: Gracz, swiat):
        # losowanie przeciwnika
        wrogowie = gracz.obecna_lokacja.potencjalni_wrogowie
        przeciwnik = wrogowie[random.randint(0, len(wrogowie) - 1)]
        przeciwnik = przeciwnik.klonuj()

        gracz_podczas = gracz.klonuj()

        print(f"> Szukasz guza i napotykasz: {przeciwnik}")

        while True:
            print(f"\tDostepne interakcje\n"
                  f"\t1. Walcz\n\t2. Perswazja\n\t3. Uciekaj")

            wybor = walidacja.waliduj_input("Co zamierzasz? ", 3) + 1
            walka = Walka(gracz_podczas, przeciwnik)

            pasywna = gracz_podczas.klasa.pasywna
            if not pasywna:
                gracz_podczas.klasa.umiejetnosc(gracz_podczas, przeciwnik)

            if wybor == 1:
                walka.wykonaj()
                gracz.zycie = gracz_podczas.zycie
                ulepsz_statystyki(gracz)
                gracz.zmiany()
                return
            elif wybor == 2:
                udalo_sie: bool = Perswazja().wykonaj(gracz_podczas, przeciwnik)
                if udalo_sie:
                    ulepsz_statystyki(gracz)
                    gracz.zycie = gracz_podczas.zycie
                    gracz.zmiany()
                    return
                else:
                    walka.oberwij()
            elif wybor == 3:
                udalo_sie: bool = Ucieczka().wykonaj(gracz_podczas, przeciwnik)
                if udalo_sie:
                    gracz.zycie = gracz_podczas.zycie
                    ulepsz_statystyki(gracz)
                    gracz.zmiany()
                    return
                else:
                    walka.oberwij()
