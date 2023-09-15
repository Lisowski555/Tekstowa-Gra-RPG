from mechaniki.akcje.zabij_czarnoksieznika import ZabijCzarnoksieznika
from mechaniki.misja import Misja
from rasy.krasnolud import Krasnolud
from rasy.rasa import Rasa
from walidacja import waliduj_input
from swiat.swiat import Swiat
from gracz import Gracz
from rasy.elf import Elf
from klasy.alkoholik import Alkoholik
from klasy.mag_ognia import MagOgnia
from klasy.asasyn import Asasyn
from klasy.berserker import Berserker
from klasy.nekromanta import Nekromanta
from klasy.paladyn import Paladyn
from klasy.klasa import Klasa
from rasy.ork import Ork
from mechaniki.akcje.tablica import Tablica
from rasy.gnom import Gnom
from rasy.drakon import Drakon
from rasy.kosmita import Kosmita
from rasy.niziolek import Niziolek
from klasy.wojownik import Wojownik
from klasy.lowca import Lowca
import re


# from swiat.lokacja import Lokacja - zbedne bo swiat ma dostep do lokacji

class Silnik:
    gracz: Gracz
    swiat: Swiat

    def __init__(self):
        self.swiat = Swiat()
        self.gracz = self.stworz_gracza()

    def graj(self):
        while True:
            lokacja = self.gracz.obecna_lokacja

            print(f"> {lokacja.opis}")
            print(f"\tWybierz dostepna akcje:")
            for i in range(len(lokacja.mozliwe_akcje)):
                print(f"\t{i + 1}. {lokacja.mozliwe_akcje[i].nazwa}")
            odp = waliduj_input("Co chcesz robic?", len(lokacja.mozliwe_akcje))
            akcja = lokacja.mozliwe_akcje[odp]
            akcja.wykonaj(self.gracz, swiat=self.swiat)
            if isinstance(akcja, ZabijCzarnoksieznika):
                self.swiat.po_koncu_gry()
            if not (not isinstance(self.gracz.zadanie, Misja) or not isinstance(akcja, Tablica)):
                self.swiat.aktywuj_zadanie()

    def stworz_gracza(self):
        imie = input(
            f"\n\tPrzystojny menzczyzno! Jak brzmi twe imie?\n\t(Jesli posiadasz w imieniu znaki specjalne,"
            f"\n\tlub polskie, nie podawaj ich gdyz zostana one usuniete. Dla komfortu oczu zas zalecamy przyjecie meskiego imienia.)"
            f"\n\t:")
        imie = "".join([ch for ch in imie if ch.isalpha()])
        imie = "".join([ch for ch in imie if ch.isascii()])
        tabu = ["Debil", "JP", "Ciota", "Cipek", "Dupek", "Daln", "Dziecko", "Murzyn", "Gnojek", "Cwel", "OVERLORD"]
        for tab in tabu:
            if re.search(tab, imie, re.IGNORECASE):
                print("Podales imie tabu, zostales wiec go pozbawiony.")
                imie = ""
        if imie.__len__() == 0:
            imie = "Bezimmienny"
        gracz = Gracz(imie)
        print(f"Nazywasz sie: {gracz.imie}")
        wybor_rasy = waliduj_input(f"\tJakiej chcialbys byc rasy?:\n\t1. Elf\n\t2. Krasnolud\n\t3. Ork\n\t4. Kosmita\n\t5. Gnom\n\t6. Niziolek\n\t7. Drakon", 7) + 1
        wybor_klasy = waliduj_input(
            f"\tJaka klasa postaci chcialbys zagrac?:\n\t1. Alkoholik\n\t2. Berserker\n\t3. Nekromanta\n\t4. Paladyn\n\t5. Mag Ognia\n\t6. Asasyn\n\t7. Lowca\n\t8. Wojownik\n\t",
            8) + 1

        rasa: Rasa
        if wybor_rasy == 1:
            rasa = Elf()
        elif wybor_rasy == 2:
            rasa = Krasnolud()
        elif wybor_rasy == 3:
            rasa = Ork()
        elif wybor_rasy == 4:
            rasa = Kosmita()
        elif wybor_rasy == 5:
            rasa = Gnom()
        elif wybor_rasy == 6:
            rasa = Niziolek()
        elif wybor_rasy == 7:
            rasa = Drakon()

        klasa: Klasa
        if wybor_klasy == 1:
            klasa = Alkoholik()
        elif wybor_klasy == 2:
            klasa = Berserker()
        elif wybor_klasy == 3:
            klasa = Nekromanta()
        elif wybor_klasy == 4:
            klasa = Paladyn()
        elif wybor_klasy == 5:
            klasa = MagOgnia()
        elif wybor_klasy == 6:
            klasa = Asasyn()
        elif wybor_klasy == 7:
            klasa = Lowca()
        elif wybor_klasy == 8:
            klasa = Wojownik()

        gracz.dodaj_ceche(rasa)
        gracz.dodaj_ceche(klasa)
        gracz.obecna_lokacja = self.swiat.pobierz_startowa_lokacje()
        return gracz
