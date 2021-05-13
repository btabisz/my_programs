imie = "Bartek"

def przywitanie(przekazane_imie):
    print(f'Cześć, {przekazane_imie}!')


def lista(przekazane_imie):
    lista = []
    lista.append(przekazane_imie)
    print(lista)


def literowana_lista(przekazane_imie):
    lista_literowa = []
    for i in przekazane_imie:
        lista_literowa.append(i)
    print(lista_literowa)


def slownik(przekazane_imie):
    slownik = {}
    slownik['imie'] = przekazane_imie
    print(slownik)


def literowany_slownik(przekazane_imie):
    a = 1
    slownik = {}
    for i in przekazane_imie:
        slownik[a] = i
        a+=1
    print(slownik)


def odwrotnie(przekazane_imie):
    print(przekazane_imie[::-1])


def plec(przekazane_imie):
    if przekazane_imie[-1] == 'a':
        print('To imię kobiety!')
    else:
        print('To imię mężczyzny!')


def dlugosc(przekazane_imie):
    print(f'Długość imienia to: {len(przekazane_imie)}')


if __name__ == '__main__':
    przywitanie(imie)
    lista(imie)
    literowana_lista(imie)
    slownik(imie)
    literowany_slownik(imie)
    plec(imie)
    dlugosc(imie)
    odwrotnie(imie)

