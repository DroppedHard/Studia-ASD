from zad5ktesty import runtests


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

runtests ( garek )