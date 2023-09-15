from walidacja import waliduj_input
from gracz import Gracz
from mechaniki.akcje.akcja import Akcja
from swiat.lokacja import Lokacja


class Podroz(Akcja):
    def __init__(self):
        super().__init__("Podroz")

    def wykonaj(self, gracz: Gracz, swiat):
        gracz.obecna_lokacja = self._podrozuj(gracz.obecna_lokacja)

    def _podrozuj(self, obecna_lokacja: Lokacja) -> Lokacja:
        print(f"> Twoja obecna lokacja to: {obecna_lokacja.nazwa}")
        print(f"\tMozesz udac sie do:")
        for i in range(len(obecna_lokacja.sasiednie_lokacje)):
            print(f"\t{i + 1}. {obecna_lokacja.sasiednie_lokacje[i].nazwa}")
        kierunek = waliduj_input("Gdzie chcesz sie udac?", len(obecna_lokacja.sasiednie_lokacje))
        return obecna_lokacja.sasiednie_lokacje[kierunek]
