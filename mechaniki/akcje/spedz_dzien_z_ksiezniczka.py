from mechaniki.akcje.akcja import Akcja


class TwojaKsiezniczka(Akcja):
    def __init__(self):
        super().__init__("Spedz dzien z Ksiezniczka")

    def wykonaj(self, gracz, swiat):
        gracz.zycie = gracz.calkowite_zycie
        print("Spedzasz dzien z Ksiezniczka, czas szybko mija.")
        return
