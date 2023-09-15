from mechaniki.akcje.akcja import Akcja
from mechaniki.misja import Misja
from walidacja import waliduj_input


class Tablica(Akcja):
    def __init__(self):
        super().__init__("Tablica")

    def wykonaj(self, gracz, swiat):
        print("Na tablicy, literka po literce odczytujesz wytyczne misji:"
              "\nPiekna zlotowlosa ksiezniczka w okolicy potrzebuje TWOJEJ pomocy."
              "\nLysy szalony czarnoksieznik porwal ja i zabral hen daleko az za pobliska pustynie!"
              "\nZ oficjalnych zrodel wiadomo, iz karmi ja rzadkimi niebieskimi grzybkami,"
              "\nktore powoduja toksyczne klonowanie! Do tego spozywanie ich wiaze sie z fatalymi skutkami ubocznymi..."
              "\nzwiarygodnych zrodel wiadomo ze jednym z tych skutkow ubocznych jest straszna klatwa..."
              "\nzas jedynym lekarstwem na klonowanie jest zapewnienie 100 procentowej pewnosci iz ksiezniczka..."
              "\nnigdy nie otrzyma krainowej daniny na dziecko przez nia wydane!"
              "\nTYLKO TY mozesz ja uratowac, zabierajac ja z rak strasznego czarnoksieznika!"
              "\n Nagroda to wieczne uwielbienie przez miasto... I REKA KSIEZNICZKI!")
        odpowiedz = waliduj_input("Czy akceptujesz misje?:\n\t1. Tak\n\t2. Nie", 2) + 1
        if odpowiedz == 1:
            gracz.zadanie = Misja()
        return
