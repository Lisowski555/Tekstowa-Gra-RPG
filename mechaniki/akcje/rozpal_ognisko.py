from mechaniki.akcje.akcja import Akcja


class RozpalOgnisko(Akcja):
    def __init__(self):
        super().__init__("Rozpal_ognisko")

    def wykonaj(self, gracz, swiat):
        gracz.zycie = gracz.calkowite_zycie
        print("Dlugi odpoczynek odnowil twoje zdrowie.")
        return
