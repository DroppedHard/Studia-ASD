"""
Polecenie:
Zadanie offline 4.
Szablon rozwiązania: zad4.py
Inwestor planuje wybudować nowe osiedle akademików.
Architekci przedstawili projekty budynków, z których inwestor musi wybrać podzbiór spełniając jego oczekiwania.
Każdy budynek reprezentowany jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b,
oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b).
W takim budynku może mieszkać h ⋅ (b − a) studentów.
Proszę zaimplementować funkcję:
def select_buildings(T, p):
...
która przyjmuje:
• Tablicę T zawierająca opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
z oznaczeniami wprowadzonymi powyżej.
• Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych
od 0), które nie zachodzą na siebie, kosztują łącznie nie więcej niż p i mieszczą maksymalną liczbę
studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja może zwrócić
dowolny z nich. Dwa budynki nie zachodzą na siebie, jeśli nie mają punktu wspólnego.
Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja
powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo
uzasadnić jej poprawność i oszacować złożoność obliczeniową.
Przykład. Dla argumentów:
T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5
wynikiem może być tablica: [ 0, 2 ]

Opis programu:
Program można podzielić na nastepujące etapy:
1. Stworzenie kopii tablicy T (sortedT), która zawiera tylko budynki o cenie mniejszej niż p.
    Do tego zapisuję wszystkie elementy w nowym formacie:
        - pod 0 indeksem jest orginalna krotka
        - indeks 1 zawiera indeks danego elementu, jaki posiada w tablicy T
        - indeks 2 zawiera pojemność studentową budynku

2. Następnie sortuję nowo utworzoną tablicę po a i b (quicksort sortujący wg 2 kryteriów).
3. Po posortowaniu tworzę nową tablicę "cache", gdzie będę zapisywał wyniki poprzednich rekurencji.
    Jest ona rozmiarów len(sortedT) na p, gdzie dynamicznie będę przypisywał wynik rekurencji "testujemy"
4. Zapisuję do odpowiednich miejsc w "cache" dane pojedynczych budynków w formacie:
    - pod indeksem 0 jest pojemnośc studentowa rozwiązania (tutaj konkretnego budynku)
    - pod indeksem 1 jest tablica indeksów budynków w tablicy T
5. Iteruję od końca tablicy sortedT w poszukiwaniu najbardziej optymalnego rozwiązania
    poprzez zastosowanie rekurencji "testujemy()". Dodatkowo by sprawdzić alternatywne rozwiązania cenowe, wykonujemy
    późniejsze polecenia z odpowiednimi warunkami (pętla while stosownie opisana)
6. Funkcja "testujemy()" szuka alternatywnych rozwiązań sprawdzając każdy budynek w prawo (rosnące a, po czym b)
    Zmienne użyte w funkcji to:
        - tab - tablica posortowanych wartośći z sortedT
        - cache - tablica "cache"
        - budzet - jest to orginalna cena
        - i - i-ty element z tablicy tab, którego analizujemy
        - p - pozostałe poieniądze na budowę rozwiązania
        - lastb - b ostatnio dodanego elementu
        - odp - tablica indeksów z T aktualnie analizowanego rozwiązania
        - poj - łączna pojemnośc studentowa rozwiązania

    Opiera się ona na warunkach zakończenia, oraz sprawdzaniu, czy:
        - można dodać nowy budynek do rozwiązania
        - czy bardziej opłaca się budynek dodać, czy lepiej nie.

7. Po znalezieniu najbardziej optymalnego rozwiązania, wynik jest zapisywany do tablicy "cache"
8. Sprawdzamy, czy nowe rozwiązanie jest najlepsze ze znalezionych do tej pory
9. Po sprawdzeniu wszystkich opcji cenowych, w tablicy "cache" kopiujemy najlepsze rozwiązania z aktualnie analizowanego
    indeksu do następnej iteracji. Dzięki temu w tablicy zachowujemy tylko najlepsze rozwiązana pod kątem pojemności
    studentowej

Jeżeli opis algorytmu jest czytany, bardzo prosiłbym o opinię o algorytmie.

Złożoność pamięciowa:
O(m + mp), gdzie 0<m<=n

Złożoność algorytmiczna: (nie mam pojęcia jak opisać poprawnie w tym przypadku)
O(n + mlogm + mp + m*m*m*p) gdzie 0<m<=n
"""

# from zad4testy import runtests


def sortT(tab, p, k):
    if p < k:
        q = partition(tab, p, k)
        sortT(tab, p, q-1)
        sortT(tab, q+1, k)


def partition(tab, p, k):
    x = tab[k][0][1]
    y = tab[k][0][2]
    i = p-1
    for j in range(p, k):
        if tab[j][0][1] < x or (tab[j][0][1] == x and tab[j][0][2] < y):    # sortowanie po a i b
            i += 1
            tab[j], tab[i] = tab[i], tab[j]

    tab[k], tab[i+1] = tab[i+1], tab[k]
    return i+1


def testujemy(tab, cache, budzet, i, p, lastb, odp, poj):
    koszt = budzet - p
    if i >= len(tab) or p == 0:
        return [poj, odp]

    if tab[i][0][1] <= lastb or tab[i][0][3] > p:
        return testujemy(tab, cache, budzet, i+1, p, lastb, odp, poj)

    if cache[i][p][0] != 0:
        for x in cache[i][p][1]:
            odp.append(x)

        return [poj + cache[i][p][0], odp]

    dodanaOdp = odp[:]
    dodanaOdp.append(tab[i][1])
    dodajemy = testujemy(tab, cache, budzet, i+1, p-tab[i][0][3], tab[i][0][2], dodanaOdp, poj + tab[i][2])
    pomijamy = testujemy(tab, cache, budzet, i+1, p, lastb, odp, poj)
    if dodajemy[0] > pomijamy[0]:
        return dodajemy

    else:
        return pomijamy


def select_buildings(T,p):
    dl = len(T)
    sortedT = []
    for x in range(dl):
        if T[x][3]<=p:               # usuwamy budynki które i tak nie kupimy
            sortedT.append((T[x], x, T[x][0]*(T[x][2]-T[x][1])))

    n = len(sortedT)
    sortT(sortedT, 0, n-1)          # sortujemy po a i b

    cache = [[[0, []] for x in range(p+1)] for _ in range(n)]
    for x in range(n):                  # ???? czy warto to robić?
        i = sortedT[x][0][3]
        while i <= p:
            cache[x][i] = [sortedT[x][2], [sortedT[x][1]]]
            i += 1


    wynik = [0, []]
    for x in range(n-1, -1, -1):
        cena = p
        while cena-sortedT[x][0][3] > 0:        # tutaj sprawdzamy alternatywne rozwiązania z niższą ceną
            temp = testujemy(sortedT, cache, cena, x+1, cena-sortedT[x][0][3], sortedT[x][0][2], [sortedT[x][1]], sortedT[x][2])
            cena = 0
            for i in temp[1]:
                cena += T[i][3]

            j = cena
            while j <= p and cache[x][j][0] < temp[0]:
                cache[x][j] = temp
                j += 1

            if wynik[0] < temp[0]:
                wynik = temp
            cena -= 1

        if x > 0:           # sprawdzamy czy nie możemy nadpisać kolejnej iteracji lepszymi wynikami
            for i in range(p+1):
                if cache[x-1][i] < cache[x][i]:
                    cache[x-1][i] = cache[x][i]

    return wynik[1]


# runtests( select_buildings )