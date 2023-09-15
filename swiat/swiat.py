from mechaniki.akcje.tablica import Tablica
from mechaniki.akcje.wyswietlstatystyki import WyswietlStatystyki
from mechaniki.akcje.zabij_czarnoksieznika import ZabijCzarnoksieznika
from mechaniki.koniec_gry import ZakonczGre
from mechaniki.akcje.podroz import Podroz
from mechaniki.akcje.rozpal_ognisko import RozpalOgnisko
from mechaniki.akcje.szukanie_guza import SzukajGuza
from przeciwnicy.ksiezniczka import Ksiezniczka
from przeciwnicy.czarnoksieznik import Czarnoksieznik
from przeciwnicy.lis_kosmita import LisKosmita
from przeciwnicy.niedzwiedz import Niedzwiedz
from przeciwnicy.wilk import Wilk
from swiat.lokacja import Lokacja


class Swiat:
    lokacje: dict

    def __init__(self):
        # inicjuje lokacje swiata
        miasto: Lokacja = Lokacja("Miasto", "Przybywasz do miasta, "
                                            "\nzapach splesnialych kartofli i odpadow wyrzucanych na ulice nieomal zwala cie z nog,"
                                            "\nna szczescie gdy przechodziles przez brame miasta straznik miejski ofiarowal ci welniana maseczke "
                                            "\ni "
                                            "\nkazal ja zalozyc na nos pod grozba kary wiezienia z powodu panujacej w miescie straszliwej choroby 'korona-lysienia', "
                                            "\nwspomnial tez cos o tablicy ogloszen...")
        las = Lokacja("Las", "Wchodzisz do zapuszczonej puszczy pelnej drzew... zwanej potocznie lasem! "
                             "\nZdajesz sie slyszec kojacy spiew szympanso-papug w oddali.")
        gory = Lokacja("Gory", "Stawiajac kolejne kroki idzie jakby ciezej, coraz wolniej... Ah! "
                               "\nCoz za rzadkie powietrze... dotarles do gorzystych gor!")
        katakumby = Lokacja("Katakumby",
                            "Stapajac ostroznie po kamiennych schodach z granitu schodzisz coraz glebiej w ciemnosc. "
                            "\nKatakumby witaja cie wilgotnym zapachem zgnilego drewna i martwych... "
                            "\nzapomnianych wspomnien.")
        pustynia = Lokacja("Pustynia", "Z kazdym kolejnym krokiem piasek pod twoimi stopami osuwa sie coraz bardziej. "
                                       "\nSlonceczko swieci prost w galki oczne, nie masz gdzie sie schowac - dotarles na stosunkowo pusta pustynie")
        wieza_czarnoksieznika = Lokacja("Wieza Czarnoksieznikow",
                                        "Przed twoimi oczami wylania sie dziwnie zakrecona lecz wysoka budowla ze spiczastym czubkiem. "
                                        "\nNieopodal kustyka czarny kot... Czy to 'Klakier'? Zastanawiasz sie wchodzac do Wiezy Czarnoksieznikow")

        # dodajemy polaczenia pomiedzy lokacjami
        miasto.dodaj_liste_sasiednich_lokacji([las, gory, katakumby, pustynia])
        las.dodaj_liste_sasiednich_lokacji([miasto, gory])
        gory.dodaj_liste_sasiednich_lokacji([miasto, las])
        katakumby.dodaj_sasiednia_lokacje(miasto)
        pustynia.dodaj_liste_sasiednich_lokacji([miasto, wieza_czarnoksieznika])
        wieza_czarnoksieznika.dodaj_sasiednia_lokacje(pustynia)

        # dodajemy przeciwnikow
        miasto.dodaj_potencjalnych_wrogow([Wilk()])
        las.dodaj_potencjalnych_wrogow([Wilk(), Niedzwiedz(), LisKosmita()])
        gory.dodaj_potencjalnych_wrogow([Niedzwiedz(), LisKosmita()])
        katakumby.dodaj_potencjalnych_wrogow([LisKosmita(), Wilk()])
        pustynia.dodaj_potencjalnych_wrogow([LisKosmita()])
        wieza_czarnoksieznika.dodaj_potencjalnych_wrogow([Ksiezniczka(), Czarnoksieznik()])

        # tworzymy akcje
        podroz = Podroz()
        guz = SzukajGuza()
        ognisko = RozpalOgnisko()
        zakoncz = ZakonczGre()
        statystyki = WyswietlStatystyki()

        tablica = Tablica()

        # dodajemy dostepne akcje
        podstawy = [podroz, guz, ognisko, statystyki, zakoncz]

        miasto.mozliwe_akcje = podstawy.copy()
        miasto.mozliwe_akcje.append(tablica)
        las.mozliwe_akcje = podstawy.copy()
        gory.mozliwe_akcje = podstawy.copy()
        katakumby.mozliwe_akcje = podstawy.copy()
        pustynia.mozliwe_akcje = podstawy.copy()
        wieza_czarnoksieznika.mozliwe_akcje = podstawy.copy()

        # dodajemy unikatowe postaci

        # dodajemy to do mapy lokacji
        self.lokacje: dict[str:Lokacja] = {
            "miasto": miasto,
            "las": las,
            "gory": gory,
            "katakumby": katakumby,
            "pustynia": pustynia,
            "wieza_czarnoksieznika": wieza_czarnoksieznika
        }

    def pobierz_startowa_lokacje(self):
        return self.lokacje["miasto"]

    def aktywuj_zadanie(self):
        wieza: Lokacja = self.lokacje["wieza_czarnoksieznika"]
        koniec = ZabijCzarnoksieznika()
        wieza.mozliwe_akcje.append(koniec)

    def po_koncu_gry(self):
        miasto: Lokacja = self.lokacje["miasto"]
        miasto.unikatowe_postacie.append(Ksiezniczka())
