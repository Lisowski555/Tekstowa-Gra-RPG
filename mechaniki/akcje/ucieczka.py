from mechaniki.interakcja import Interakcja
from mechaniki.kostka import *


class Ucieczka(Interakcja):
    def __init__(self):
        super().__init__("Ucieczka")

    def wykonaj(self, gracz, przeciwnik):
        ty = d20() + modyfikator(gracz.zwinnosc)
        wrog = d20() + modyfikator(przeciwnik.zwinnosc)
        print(f"Twoj rzut to: {ty}\tkontra: {wrog}")
        if ty > wrog:
            print(f"{gracz.imie} ucieka w poplochu!")
            return True
        else:
            print("Zostales zlapany cwaniaczku.")
            return False
