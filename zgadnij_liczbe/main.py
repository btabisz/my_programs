from random import randint

def zgadnij_liczbe():
    szukana_liczba = randint(1, 300)
    #print(f'Szukana liczba to: {szukana_liczba}')
    dopuszczalna_liczba_prob = 7

    while dopuszczalna_liczba_prob > 0:
        print(f'Liczba pozostałych szans: {dopuszczalna_liczba_prob}')
        podana_liczba = int(input("Podaj Liczbę:"))
        if podana_liczba == szukana_liczba:
            print(f'Brawo - to jest szukana liczba!')
            exit(0)
        if  szukana_liczba > podana_liczba:
            print(f'Szukana liczba jest wieksza od wpisanej')
            dopuszczalna_liczba_prob -= 1
        if szukana_liczba < podana_liczba:
            print(f'Szukana liczba jest mniejsza od podanej')
            dopuszczalna_liczba_prob -= 1
    else:
        print(f'Przegrałeś - koniec gry! Szukana liczba {szukana_liczba}')


if __name__ == '__main__':
    zgadnij_liczbe()


