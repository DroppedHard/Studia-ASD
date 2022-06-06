"""
Polecenie:
Zadanie offline 9.
Szablon rozwiązania: zad9.py
W pewnym państwie znajdują się miasta, połączone siecią jednokierunkowych rurociągów, każdy o
określonej przepustowości. Złoża ropy zostały wyczerpane, jednak w jednym z miast odkryto niewyczerpane źródło nowego
rodzaju paliwa. Postanowiono zbudować dwie fabryki w różnych miastach oczyszczające nowe paliwo.
Z pewnych względów fabryki te nie mogą znajdować się w mieście,w którym odkryto nowe złoża i nowe paliwo będzie
transportowane istniejącą siecią rurociągów. Należy wskazać dwa miasta w których należy zbudować fabryki aby
zmaksymalizować produkcję oczyszczonego paliwa.
Proszę zaimplementować funkcję maxflow(G,s), która dla istniejącej sieci rurociągów G i miasta,
w którym odkryto złoże s, zwróci maksymalną łączną przepustowość do dwóch miast w których należy zbudować fabryki.
Miasta są ponumerowane kolejnymi liczbami 0, 1, 2, ... Sieć rurociągów opisuje lista trójek:
(miasto w którym rozpoczyna się rurociąg, miasto w którym się kończy rurociąg, przepustowość rurociągu)
Przykład Dla sieci G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)] oraz miasta s=2 wynikiem jest 25 (miasta 4 i 5).

Opis programu:
Program polega na zastosowaniu algorytmu Edmonds-Karpa. Polega on na sprawdzeniu wszystkich par a i b i wypisaniu
największego możliwego przepływu. Program zawiera kilka optymalizacji:
1. badamy ujścia z miasta s i sprawdzamy maksymalny i minimalny przepływ możliwy.
    Maksymalny - suma wszystkich ujść z S
    Minimalny - suma 2 największych ujść z S
2. Jeśli S ma 2 lub mniej ujść, to odpowiedzią jest suma tych ujść.
3. dla każdej pary a i b należącej do zbioru miast:
    jeśli suma wpływających kanalizacji z innych miast niż a i b jest większa niż minimum, to jest szansa że ta para
    jest dobrą odpowiedzią. W przeciwnym wypadku ta para nigdy nie osiągnie takiego wyniku jak 2 sąsiadów z
    najlepszym przepływem wychodzącym z S.
4. Jeśli przepływ dla aktualnie rozpatrywanej pary jest równy maksimum, to zwracamy maksimum i kończymy szukanie takiej
pary.

funkcje:
sciezka - wykonuje zamysł znalezienia ścieżki powiększającej w algorytmie.
przeplyw - sprawdza jaki jest przepływ zgodnie z algorytmem.

Złożonośc algorytmu:
Pamięciowa: O(1/2 * (V^2)^2) - CHYBA bo co każdą iterację tworzę kopię sieci residualnej aby rozpatrzyć kazdy przypadek.
Czasowa: O(V^2 * (V+E)) = O(V^3+EV^2)
"""
# from zad9testy import runtests
from queue import PriorityQueue
from collections import deque


def sciezka(mac, parent, poj, x):
    while parent[x] != -1:
        mac[x][parent[x]] += poj
        mac[parent[x]][x] -= poj
        x = parent[x]


def przeplyw(mac,s,a,b):
    odp = 0
    koniec = False
    while not koniec:
        jestsciezka = False
        n = len(mac)
        parent = [None for _ in range(n)]
        inf = float("inf")
        pojemnosc = [inf for _ in range(n)]
        parent[s] = -1
        queue = deque()
        queue.append(s)
        lenq = 1
        while lenq > 0:
            u = queue.popleft()
            lenq-=1
            for v in range(n):
                if mac[u][v] == 0:
                    continue

                if v == a:
                    jestsciezka = True
                    parent[v] = u
                    pojemnosc[v] = min(pojemnosc[u], mac[u][v])
                    sciezka(mac, parent, pojemnosc[v], a)
                    odp += pojemnosc[v]
                    queue.clear()
                    lenq = 0
                    break

                elif v == b:
                    jestsciezka = True
                    parent[v] = u
                    pojemnosc[v] = min(pojemnosc[u], mac[u][v])
                    sciezka(mac, parent, pojemnosc[v], b)
                    odp += pojemnosc[v]
                    queue.clear()
                    lenq = 0
                    break

                elif parent[v] is None:
                    parent[v] = u
                    pojemnosc[v] = min(pojemnosc[u], mac[u][v])
                    queue.append(v)
                    lenq+=1

        if not jestsciezka:
            koniec = True

    return odp


def maxflow( G,s ):
    v = s
    for e in G:
        if e[0] > v:
            v = e[0]
        if e[1] > v:
            v = e[1]

    residualna = [[0 for i in range(v+1)] for _ in range(v+1)]

    maximum = 0
    minimumpq = PriorityQueue()
    minimum = 0
    for e in G:
        residualna[e[0]][e[1]] = e[2]
        if e[0] == s:
            maximum += e[2]
            minimumpq.put(e[2]*-1)

    if minimumpq.qsize()<=2:
        return maximum
    else:
        minimum = (minimumpq.get()+minimumpq.get())*-1

    odp = 0
    for i in range(v+1):
        for j in range(i+1, v+1):
            if i != s and j != s:
                # liczymy pojemność i, j:
                cp = [row[:] for row in residualna]
                capacity = 0
                for x in range(v+1):
                    capacity += cp[x][i] + cp[x][j]

                capacity -= residualna[i][j] + residualna[j][i]
                # jeśli minimum jest większe niż wejście z pozostałych wierzchołków do i, j to ignorujemy tą iterację
                if capacity >= minimum:
                    temp = przeplyw(cp, s, i, j)
                    if temp > odp:
                        odp = temp
                        if odp == maximum:
                            return odp
                else:
                    continue

    return odp


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( maxflow, all_tests = True )