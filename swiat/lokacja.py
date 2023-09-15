from typing import List

from mechaniki.akcje.akcja import Akcja


class Lokacja:
    def __init__(self, nazwa, opis):
        self.nazwa = nazwa
        self.opis = opis
        self.sasiednie_lokacje: List[Lokacja] = []
        self.mozliwe_akcje: List[Akcja] = []
        self.unikatowe_postacie = []
        self.potencjalni_wrogowie = []

    def dodaj_sasiednia_lokacje(self, lokacja):
        self.sasiednie_lokacje.append(lokacja)

    def dodaj_liste_sasiednich_lokacji(self, lokacje):
        self.sasiednie_lokacje.extend(lokacje)

    def dodaj_potencjalnych_wrogow(self, wrogowie):
        self.potencjalni_wrogowie = wrogowie
