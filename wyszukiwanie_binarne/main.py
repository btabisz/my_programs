p = [3, 10, -6, 0, 8, 122, 14, -30, 12, 4, 200]

s = sorted(p)
print(s)

szukana =int(input("podaj liczbę"))

lewy = 0
prawy = len(s) - 1


while lewy <= prawy:
    srodkowy = (lewy + prawy) // 2
    if s[srodkowy] == szukana:
        print(f'Szukana liczba ({szukana}) jest na liście! ')
        break
    elif s[srodkowy] < szukana:
        lewy = srodkowy + 1
    else:
        prawy = srodkowy - 1
else:
    print(f'Liczby {szukana} nie ma na liście!')

