"""
Polecenie:
Zadanie offline 7.
Szablon rozwiązania: zad7.py
Dane jest N miast, każde miasto jest otoczone murem, w którym znajdują się dwie bramy: północna
i południowa. Jeżeli przyjedziemy do miasta jedną z bram musimy wyjechać z niego tą drugą.
Wyjeżdżając każdą z bram można dojechać bezpośrednio do jednego lub więcej innych miast.
Proszę zaproponować i zaimplementować algorytm który sprawdza czy wyruszając z jednego z
miast można odwiedzić wszystkie miasta dokładnie jeden raz i powrócić do miasta, z którego się
wyruszyło. Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo
uzasadnić jego poprawność i oszacować złożoność obliczeniową.
Algorytm należy zaimplementować jako funkcję:
def droga(G):
...
która przyjmuje sieć połączeń G pomiędzy miastami i zwraca listę numerów odwiedzanych miast
albo None jeśli takiej drogi nie ma. Sieć połączeń jest dana w postaci listy, która dla każdego
miasta zawiera dwie listy: miast dostępnych z bramy północnej oraz miast dostępnych z bramy
południowej. Miasta numerowane są od 0.
Przykład. Dla argumentów:
G = [ ([1],[2,3,4]),
([0],[2,5,6]),
([1,5,6],[0,3,4]),
([0,2,4],[5,7,8]),
([0,2,3],[6,7,9]),
([1,2,6],[3,7,8]),
([1,2,5],[4,7,9]),
([4,6,9],[3,5,8]),
([3,5,7],[9]),
([4,6,7],[8]) ]
wynikiem jest np. lista: ([ 0, 1, 5, 7, 9, 8, 3, 2, 6, 4 ])

Opis programu:
Zadanie rozwiązałem korzystając z DFS-a z lekkim dodatkiem.
Zaczynam od miasta 0 i sprawdzam wszystkich północnych sasiadów (można zacząć od dowolnej bramy, musimy znaleźć
jakikolwiek cykl). Więc jeśli istnieje, to nie ma znaczenia od którego miasta zaczniemy, ani od której bramy.
Następnie sprawdzam rekurencyjnie czy możemy utworzyć cykl (podobnie jak DFS, czyli idę najdalej jak mogę szukając
miasta 0). Jednocześnie do rekurencji podaję którą bramą musimy wyjść z i-tego miasta.
Jeśli rekurencja nie znalazła cyklu (czyli nie wróciła do 0-wego miasta) to zwraca None. W przeciwnym wypadku zwraca od
razu pierwszy znaleziony cykl spełniający warunki zadania.

Złożoność pamięciowa: O(n) gdzie n to liczba miast
Złożonośc obliczeniowa: (chyba) O(n^2)
"""
# from zad7testy import runtests


def cykl(G, n, tab, i, brama, counter):
    tab[i] = True
    gdzie = 0
    if brama:
        gdzie = 1

    if counter == n:
        if 0 in G[i][gdzie]:
            return [i]
        else:
            return None

    for x in G[i][gdzie]:
        if tab[x]:
            continue
        else:
            odp = None
            if i in G[x][0]:
                odp = cykl(G, n, tab, x, True, counter+1)
            elif i in G[x][1]:
                odp = cykl(G, n, tab, x, False, counter+1)
            if odp is not None:
                odp.append(i)
                return odp
    tab[i] = False
    return None


def droga(G):
    n = len(G)
    odwiedzone = [False for _ in range(n)]
    # zaczynamy od miasta 0     False - północna, True - południowa. Do funkcji przekazujemy którą bramą mamy wyjść
    # początek od 0 jest hard-coded. Trzeba będzie zmienić jesli trzeba
    odp = None
    el = G[0]
    counter = 1
    odwiedzone[0] = True
    for north in el[0]:
        if 0 in G[north][0]:
            odp = cykl(G, n, odwiedzone, north, True, counter+1)
        elif 0 in G[north][1]:
            odp = cykl(G, n, odwiedzone, north, False, counter+1)
        if odp is not None:
            break

    if odp is not None:
        odp.append(0)

    return odp


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( droga, all_tests = True )