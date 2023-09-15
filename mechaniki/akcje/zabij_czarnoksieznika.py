from mechaniki.akcje.akcja import Akcja
from mechaniki.akcje.spedz_dzien_z_ksiezniczka import TwojaKsiezniczka
from mechaniki.akcje.szukanie_guza import SzukajGuza
from mechaniki.akcje.walka_z_czarnoksieznikiem import WalkaZCzarnoksieznikiem
from przeciwnicy.czarnoksieznik import Czarnoksieznik
from przeciwnicy.ksiezniczka import Ksiezniczka
from swiat.lokacja import Lokacja


class ZabijCzarnoksieznika(Akcja):
    def __init__(self):
        super().__init__("Staw czola strasznemu i lysemu Czarnoksieznikowi")

    def wykonaj(self, gracz, swiat):
        wieza = Lokacja("Wieza Czarnoksieznika",
                        "Przed twoimi oczami wylania sie dziwnie zakrecona lecz wysoka budowla ze spiczastym czubkiem."
                        " Nieopodal biega czarny kot..."
                        " Czy to 'Klakier'? Zastanawiasz sie wchodzac do Wiezy Czarnoksieznika")
        wieza.dodaj_potencjalnych_wrogow([Czarnoksieznik()])
        poprzednia_lokacja = gracz.obecna_lokacja
        gracz.obecna_lokacja = wieza
        guz = WalkaZCzarnoksieznikiem()
        guz.wykonaj(gracz, swiat)
        gracz.obecna_lokacja = poprzednia_lokacja
        gracz.zadanie.misja_zakonczona()
        swiat.lokacje["miasto"].unikatowe_postacie = [Ksiezniczka()]
        swiat.lokacje["miasto"].mozliwe_akcje.append(TwojaKsiezniczka())
        return
