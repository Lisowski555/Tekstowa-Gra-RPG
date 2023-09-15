import copy

from rasy.rasa import Rasa
from klasy.klasa import Klasa
from swiat.lokacja import Lokacja


class Gracz:
    klasa: Klasa
    rasa: Rasa
    obecna_lokacja: Lokacja
    zadanie = False

    tabela_statystyk: list

    def __init__(self, imie="Bezimienny"):
        self.imie = imie
        self.zycie = 30
        self.calkowite_zycie = self.zycie
        self.sila = 10
        self.zwinnosc = 10
        self.zbroja = 10
        self.inteligencja = 10
        self.charyzma = 10

        self.tabela_statystyk = [self.calkowite_zycie, self.sila, self.zwinnosc,
                                 self.zbroja, self.inteligencja,
                                 self.charyzma]

    def najlepszy_atak(self):
        return max(self.sila, self.inteligencja, self.zwinnosc)

    def dodaj_ceche(self, co: Klasa or Rasa):
        if isinstance(co, Klasa):
            self.klasa = co
        else:
            self.rasa = co

        self.zycie += co.zycie
        self.calkowite_zycie += co.zycie
        self.sila += co.sila
        self.zwinnosc += co.zwinnosc
        self.inteligencja += co.inteligencja
        self.charyzma += co.charyzma
        self.zbroja += co.zbroja

        self.tabela_statystyk = [self.calkowite_zycie, self.sila, self.zwinnosc,
                                 self.zbroja, self.inteligencja,
                                 self.charyzma]

    def klonuj(self):
        klon = copy.deepcopy(self)
        return klon

    def zmiany(self):
        t = self.tabela_statystyk
        self.calkowite_zycie = t[0]
        self.sila = t[1]
        self.zwinnosc = t[2]
        self.zbroja = t[3]
        self.inteligencja = t[4]
        self.charyzma = t[5]
