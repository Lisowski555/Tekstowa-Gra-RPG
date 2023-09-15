from mechaniki.interakcja import Interakcja
from mechaniki.kostka import *


class Perswazja(Interakcja):

    def __init__(self):
        super().__init__("Perswazja")

    def wykonaj(self, gracz, przeciwnik):
        ty = d20() + modyfikator(gracz.charyzma)
        wrog = d20() + modyfikator(przeciwnik.charyzma)
        print(f"Twoj rzut to: {ty}\tkontra: {wrog}")
        if ty > wrog:
            print(f"{przeciwnik.__str__()} po dlugim perswadowaniu pozwala ci odejsc.")
            return True
        else:
            print("Nie udalo sie, tym razem ladny usmiech nie pomogl.")
            return False
