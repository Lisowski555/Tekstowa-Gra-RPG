from mechaniki.akcje.akcja import Akcja


class WyswietlStatystyki(Akcja):
    def __init__(self):
        super().__init__("Wyswietl_statystyki")

    def wykonaj(self, gracz, swiat):
        print(
            f"{gracz.imie}, twoje statystyki to:\n\tAktualne zycie: {gracz.zycie}",
            f"\n\tMaksymalne zycie: {gracz.calkowite_zycie}\n\tSila: {gracz.sila}",
            f"\n\tZwinnosc: {gracz.zwinnosc}\n\tZbroja: {gracz.zbroja}\n\tInteligencja: {gracz.inteligencja}\n\tCharyzma: {gracz.charyzma}")
        return

