# from zad5ktesty import runtests
"""
Zadanie 5 - Ograj Garka
Szablon rozwiązania: zad5k.py
Dana jest talia N kart wyrażona poprzez tablicę A liczb naturalnych zawierającą wartości tych kart. Można przyjąć, że talia posiada parzystą ilość kart. Karty zostały rozłożone na bardzo szerokim stole w kolejności pojawiania się w tablicy. Dziekan poinformował Cię, że podwyższy Ci ocenę z WDI o pół stopnia, jeżeli wygrasz z nim w pewną grę, polegającą na braniu kart z jednego lub drugiego końca stołu na zmianę. Zakładając, że zaczynasz rozgrywkę, musisz znaleźć jaką maksymalnie sumę wartości kart uda Ci się uzyskać. Jednak, co ważne, musisz przyjąć, że dziekan jest osobą bardzo inteligentną i także będzie grał w 100% na tyle optymalnie, na tyle to możliwe. Aby nie oddawać losu w ręce szczęścia postanowiłeś, że napiszesz program, który zagwarantuje Ci wygraną (lub remis). Twój algorytm powinien powiedzieć Ci, jaka jest maksymalna suma wartości kart, którą masz szansę zdobyć grając z Garkiem.
Algorytm należy zaimplementować jako funkcję postaci:
def garek( A ): …
która przyjmuje tablicę liczb naturalnych T i zwraca liczbę będącą maksymalną możliwą do uzyskania sumą wartości kart.
Przykład. Dla tablicy:
T = [8, 15, 3, 7]
Wynikiem jest liczba 22
"""

def ezwin(tab, a, b, cache):
    if cache[a][b] is not None:
        return cache[a][b]
    elif a == b:
        cache[a][b] = (tab[a], 0)
    elif a+1 == b:
        cache[a][b] = (max(tab[a], tab[b]), min(tab[a], tab[b]))
    else:
        lewo = ezwin(tab, a + 1, b, cache)
        prawo = ezwin(tab, a, b - 1, cache)
        if lewo[1] + tab[a] > prawo[1] + tab[b]:
            cache[a][b] = (lewo[1] + tab[a], lewo[0])
        elif lewo[1] + tab[a] <= prawo[1] + tab[b]:
            cache[a][b] = (prawo[1] + tab[b], prawo[0])

    return cache[a][b]


def garek ( A ): # talia ma parzystą liczbę kart - my rozpoczynamy rozgrywkę
    n = len(A)
    cache = [[None for _ in range(n)] for x in range(n)]
    odp = ezwin(A, 0, n-1, cache)
    print(odp)
    return odp[0]

# runtests ( garek )
