from mechaniki.akcje.akcja import Akcja


class ZakonczGre(Akcja):
    def __init__(self):
        super().__init__("Zakoncz")

    def wykonaj(self, gracz, swiat):
        print(f"> Przytloczony zlem otaczajacego cie swiata wykonales honorowo seppuku.\n"
              f"  Mieszkancy miasta postawili ci pominik pamieci z drewniana tabliczka mowiaca:\n"
              f"  Honorowy {gracz.imie} nie wytrzymal i kopnal w kalendarz")
        exit(0)
