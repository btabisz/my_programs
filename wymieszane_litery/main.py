import random

slowa = ['kubek', 'fotel', 'lustro', 'obraz']

def wymieszane_litery():
    szukane_slowo = random.choice(slowa)
    lista_szukane_slowo = []
    lista_wymieszane_slowo = []
    for i in szukane_slowo:
        lista_szukane_slowo.append(i)
    while len(lista_szukane_slowo) > 0:
        losowy_index = random.randint(0, len(lista_szukane_slowo)-1)
        lista_wymieszane_slowo.append(lista_szukane_slowo[losowy_index])
        lista_szukane_slowo.remove(lista_szukane_slowo[losowy_index])
    wymieszane_slowo = ''.join(lista_wymieszane_slowo)
    print(f'Odgadnij jakie to słowo: {wymieszane_slowo}?')
    pozostale_proby = 10
    while pozostale_proby > 0:
        print(f'Pozostałe próby: {pozostale_proby}')
        podane_slowo = input(f"Wprowadź słowo:")
        if podane_slowo == szukane_slowo:
            print('Brawo!')
            exit(0)
        else:
            print('Pudło!')
            pozostale_proby -= 1
    else:
        print('Przegrałeś!')


if __name__ == '__main__':
    wymieszane_litery()

