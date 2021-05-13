import random

def rzut_moneta():
    liczba_rzutow = 0
    orzel = 0
    reszka = 0
    while liczba_rzutow < 100:
        moneta = ['orzel', 'reszka']
        wylosowana_strona = random.choice(moneta)
        liczba_rzutow += 1
        if wylosowana_strona == "orzel":
            orzel += 1
        else:
            reszka += 1
    else:
        print(f'orzel = {orzel}, reszka = {reszka}, suma = {orzel + reszka}')


if __name__ == '__main__':
    rzut_moneta()


