"""
Polecenie:
Zadanie offline 8.
Szablon rozwiązania: zad8.py
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad,
tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii
prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
√
(x1 − x2)
2 + (y1 − y2)
2.
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej
w km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni
dzielącą otwarcie pierwszej i ostatniej autostrady.
Przykład Dla tablicy A =[(10,10),(15,25),(20,20),(30,40)] wynikiem jest 7 (Autostrady pomiędzy miastami 0-1, 0-2, 1-3).

Opis algorytmu
Algorytm opiera się troche na algorytmie Kruskala.
Działanie:
1. Dodajemy do tablicy V wszystkie możliwe krawędzie (n po 2 możliwości) i je sortujemy po czasie tworzenia autostrady.
Zapisujemy jako krotkę z czasem budowania i jakie miasta łączy.
2. bazując na algorytmie Kruskala szukamy minimalnego drzewa rozpinającego, gdzie kosztem jest czas wykonania autostrady
2.1. Bierzemy pierwsze n-1 krawędzi i analizujemy czy graf jest spójny. Jeśli tak, to sprawdzamy ile jeszcze możemy
krawędzi usunąć (od lewej strony tabeli posortowanej rosnąco) aby zachować spójność grafu. Dla otzrymanego wyniku
sprawdzamy różnicę największego i najmniejszego kosztu i zapisujemy jako odpowiedź, jeśli jest ona mniejsza niż
poprzednio znaleziona opcja.
2.2. Spójnośc sprawdzam analizując pewien zakres krawędzi. Zapisuję to w formacie zbiorów, gdzie w odpowiednich
zbiorach zawierają się wierzchołki tworzące spójny podgraf. Każdą nową krawędź analizujemy, i są 4 możliwości:
    - cała krawędź zawiera się w zbiorze
    - jedna część krawędzi zawiera się w zbiorze, a druga nie zawiera się nigdzie
    - nowa krawędź łączy dwa zbiory
    - krawędź tworzy nowy zbiór (żaden wierzchołek nie należy nigdzie)
Po przeanalizowaniu wszystkich opcji, wypisujemy najmniejszą.

złożonośc pamięciowa: O(V+n)
złożoność czasowa: O(n^2 + V^2) ~O(V^2)
"""
# from zad8testy import runtests


def spojny_poczatek(tab, n, p, k):  # funkcja zwraca maksymalny początkowy indeks dla którego graf dalej jest spójny
    zasieg = [[tab[k][1], tab[k][2]]]   # działanie jest takie same jak sprawdzanie spójności (opis od 99 linijki)
    for i in range(k-1, p, -1):         # tylko algorytm idzie od prawej do lewej
        e1 = [tab[i][1], None]
        e2 = [tab[i][2], None]
        znaleziono = False
        for j in range(len(zasieg)):
            if e1[0] in zasieg[j] and e2[0] in zasieg[j]:
                znaleziono = True
                break
            elif e1[0] in zasieg[j] and e2[0] not in zasieg[j]:
                if e1[1] is None:
                    znaleziono = True
                    zasieg[j].append(e2[0])
                    e2[1] = j
                else:
                    temp = list(set(zasieg[e1[1]] + zasieg[j]))
                    zasieg[e1[1]] = temp
                    del zasieg[j]
                    break
            elif e1[0] not in zasieg[j] and e2[0] in zasieg[j]:
                if e2[1] is None:
                    znaleziono = True
                    zasieg[j].append(e1[0])
                    e1[1] = j
                else:
                    temp = list(set(zasieg[e2[1]] + zasieg[j]))
                    zasieg[e2[1]] = temp
                    del zasieg[j]
                    break

        if not znaleziono:
            zasieg.append([e1[0], e2[0]])
        elif (e1[1] is not None and n == len(zasieg[e1[1]])) or (e2[1] is not None and n == len(zasieg[e2[1]])):
            return i    # tylko zwraca indeks dla którego graf jest spójny

    return False    # zwraca fałsz jeśli coś poszło nie tak (nigdy nie powinno to się wydarzyć, bo
                    # przedział zawiera graf spójny)


def ceil(n):    # zwraca sufit z danej wartości, trywialne
    if int(n) < n:
        return int(n) + 1
    else:
        return int(n)


def merge(tab1, tab2):      # łączy 2 tablice bez powtarzających się elementów - mergesort
    tab1.sort()
    tab2.sort()
    odp = []
    n1 = len(tab1)
    n2 = len(tab2)
    x, y = 0, 0
    while x < n1 and y < n2:
        if tab1[x] == tab2[y]:
            odp.append(tab1[x])
            x += 1
            y += 1
        elif x == n1 or tab1[x] > tab2[y]:
            odp.append(tab2[y])
            y += 1
        elif y == n2 or tab2[y] > tab1[x]:
            odp.append(tab1[x])
            x+=1

    while x == n1 and y != n2:
        odp.append(tab2[y])
        y += 1

    while x != n1 and y == n2:
        odp.append(tab1[x])
        x += 1

    return odp


def highway(A):
    n = len(A)

    V = [0 for _ in range(n*(n-1)//2)]
    countV = 0
    for i in range(n):          # Dodajemy wszystkie możiwe krawędzie do tablicy V (bierzemy niepowtarzające się kraw.)
        for j in range(i):
            temp = (ceil(((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5), i, j)
            V[countV] = temp
            countV += 1

    V.sort()        # sortujemy je - do algorytmu Kruskala

    p, k = 0, n-2   # spójny graf o najmniejszej liczbie krawędzi ma ich n-1
    odp = float("inf")
    while k < countV:   # sprawdzamy wszystkie opcje krawędzi
        zasieg = [[V[p][1], V[p][2]]]   # tutaj zapisujemy zbiory wierzchołków w jakie się łączą
        spojne = False
        for i in range(p + 1, k + 1):   # sprawdza spójność grafu z wykorzystaniem krawędzi od p do k
            e1 = [V[i][1], None]
            e2 = [V[i][2], None]
            znaleziono = False      # przechowuje boolean, czy krawędź należy do jakiegokolwiek ze zbiorów
            for j in range(len(zasieg)):    # sprawdzamy wszystkie zbiory i w zależności od analizowanej krawędzi:
                if e1[0] in zasieg[j] and e2[0] in zasieg[j]:   # krawędź cała zawiera się w j-tym zbiorze
                    znaleziono = True
                    break
                elif e1[0] in zasieg[j] and e2[0] not in zasieg[j]: # jedna część krawędzi znajduje się w zbiorze
                    if e1[1] is None:   # jesli nie znaleźliśmy gdzie naleźy drugi koniec
                        znaleziono = True
                        zasieg[j].append(e2[0])     # dodajemy drugi koniec do zbioru
                        e2[1] = j       # zapisujemy gdzie doaliśmy ten koniec
                    else:   # jeśli drugi koniec dodaliśmy już wcześniej do zbioru, to ta krawędź łączy nam wierzch.
                        temp = merge(zasieg[e1[1]], zasieg[j])  # łączymy wszystkie wierzchołki usuwając powtórzenia
                        zasieg[e1[1]] = temp    # nadpisujemy wcześniejszą tablicę połączoną
                        del zasieg[j] # usuwamy aktualnie przeglądaną tablicę i kończymy pętlę
                        break
                elif e1[0] not in zasieg[j] and e2[0] in zasieg[j]: # analogicznie, tylko dla drugiego końca krawędzi
                    if e2[1] is None:
                        znaleziono = True
                        zasieg[j].append(e1[0])
                        e1[1] = j
                    else:
                        temp = merge(zasieg[e2[1]], zasieg[j])
                        zasieg[e2[1]] = temp
                        del zasieg[j]
                        break

            if not znaleziono:  # jeśli krawędź nie jest spójna z poprzednimi, to tworzymy nowy zbiór
                zasieg.append([e1[0], e2[0]])
            elif (e1[1] is not None and n == len(zasieg[e1[1]])) or (e2[1] is not None and n == len(zasieg[e2[1]])):
                spojne = True   # jesli nowo dodana krawędź utworzyła zbiór ze wszystkimi wierzchołkami to jest to
                                # spójny graf

        while k < countV-1 and not spojne:      # sprawdzamy czy k+1 krawędź utworzy nam graf spójny
            k += 1                              # algorytm ten sam jak wyżej, tylko analizujemy jedną krędź
            e1 = [V[k][1], None]
            e2 = [V[k][2], None]
            znaleziono = False
            for j in range(len(zasieg)):
                if e1[0] in zasieg[j] and e2[0] in zasieg[j]:
                    znaleziono = True
                    break
                elif e1[0] in zasieg[j] and e2[0] not in zasieg[j]:
                    if e1[1] is None:
                        znaleziono = True
                        zasieg[j].append(e2[0])
                        e2[1] = j
                    else:
                        temp = merge(zasieg[e1[1]], zasieg[j])
                        zasieg[e1[1]] = temp
                        del zasieg[j]
                        break
                elif e1[0] not in zasieg[j] and e2[0] in zasieg[j]:
                    if e2[1] is None:
                        znaleziono = True
                        zasieg[j].append(e1[0])
                        e1[1] = j
                    else:
                        temp = merge(zasieg[e2[1]], zasieg[j])
                        zasieg[e2[1]] = temp
                        del zasieg[j]
                        break

            if not znaleziono:
                zasieg.append([e1[0], e2[0]])
            elif (e1[1] is not None and n == len(zasieg[e1[1]])) or (e2[1] is not None and n == len(zasieg[e2[1]])):
                spojne = True

        p = spojny_poczatek(V, n, p, k)    # funkcja zwracająca maksymalny indeks "p" dla którego graf dalej jest spójny

        temp = V[k][0] - V[p][0]
        if odp > temp:      # zapisujemy minimalną różnicę
            odp = temp

        p += 1  # przeskakujemy przedziałem o 1 w prawo - zakończyliśmy pętlę na pseudo-drzewie rozpinającym
        k += 1

    return odp


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(highway, all_tests=True)