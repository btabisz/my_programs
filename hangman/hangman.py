import random

zbior_slow = ["prawy", "telewizor", "internet", "python", "arbuz", "mama", "tata"]
wylosowane_slowo = random.choice(zbior_slow)
# print(wylosowane_slowo)
zakryte_slowo = []
szanse = 10
for i in wylosowane_slowo:
    zakryte_slowo.append("_")

def hangman():
    pozostale_szanse = szanse
    while not wylosowane_slowo == str(''.join(zakryte_slowo)):
        print("Szukamy słowa:")
        print(' '.join(zakryte_slowo))
        print(f'Pozostałe szanse: {pozostale_szanse}')
        print("Podaj literkę:")
        podana_literka = str(input())
        if podana_literka == wylosowane_slowo:
            print(f'Gratulacje, szukane słowo to {wylosowane_slowo}!!!')
            return exit(0)
        for i in range(0, len(wylosowane_slowo)):
            if wylosowane_slowo[i] == podana_literka:
                zakryte_slowo[i] = podana_literka
        if wylosowane_slowo == str(''.join(zakryte_slowo)):
            print(f'Gratulacje, szukane słowo to {wylosowane_slowo}!!!')
        pozostale_szanse -= 1
        if pozostale_szanse == 0:
            print(f'Niestety, szanse się skończyły. Szukane słowo to {wylosowane_slowo}!!!')
            return exit(0)


hangman()