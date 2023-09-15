import random

from gracz import Gracz
from ustawienia import *


def d20():
    return random.randint(1, 20)


def d4():
    return random.randint(1, 4)


def d6():
    return random.randint(1, 6)


def modyfikator(stat):
    return int(stat / 2 - 5)


def ulepsz_statystyki(gracz: Gracz):
    rand = random.randint(1, 10)
    try:
        if rand <= Ustawienia.szansa_na_statystyke:
            dlugosc = int(gracz.tabela_statystyk.__len__())
            index = random.randint(0, dlugosc - 1)
            gracz.tabela_statystyk[index] += Ustawienia.ulepszenie_statystyki
    except:
        raise ValueError(f"Wywalilem sie bo dlugosc to {dlugosc} a lista {gracz.tabela_statystyk.__len__()} i index: {index}" ) #wywalaj znowu