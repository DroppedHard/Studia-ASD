from zad3ktesty import runtests


def kladna(tab, i, k, cache):
    if i-k < 0:
        # print(i, k)
        return tab[i]
    else:
        odp = float("inf")
        for x in range(i-k, i):
            # print(cache[x])
            odp = min(odp, cache[x])

        return odp + tab[i]


def ksuma( T, k ):
    # print(T, k)
    n = len(T)
    ladnasuma = 0
    if k == 1:
        ladnasuma = sum(T)
    elif k == n:
        ladnasuma = min(T)
    else:
        wynik = [0 for _ in range(n)]
        for i in range(n):
            wynik[i] = kladna(T, i, k, wynik)

        ladnasuma = float("inf")

        for i in range(n-k, n):
            ladnasuma = min(ladnasuma, wynik[i])

    return ladnasuma


runtests ( ksuma )