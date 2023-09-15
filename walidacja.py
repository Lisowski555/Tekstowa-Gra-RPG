def waliduj_input(komunikat, liczba_opcji) -> int:
    surowy_input = input(f"\t{komunikat} :")
    try:
        result = int(surowy_input) - 1
        if result < 0 or result >= liczba_opcji:
            raise IndexError
        return result
    except:
        print("\tNiepoprawna wartosc")
        return waliduj_input(komunikat, liczba_opcji)
