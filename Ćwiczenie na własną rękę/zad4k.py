from zad4ktesty import runtests


def uwalanie(tab, n, i, j, cache):
    if i == j == 0:
        return 0
    if i < 0 or j < 0:
        return float("inf")
    if cache[i][j] is not None:
        return cache[i][j]
    cache[i][j] = min(uwalanie(tab, n, i-1, j, cache), uwalanie(tab, n, i, j-1, cache)) + tab[i][j]
    return cache[i][j]
    # if i == j == n-1:
    #     return 0
    # elif i == n-1:
    #     return uwalanie(tab, n, i, j+1, cache) + tab[i][j]
    # elif j == n-1:
    #     return uwalanie(tab, n, i+1, j, cache) + tab[i][j]
    # else:
    #     return min(uwalanie(tab, n, i+1, j, cache), uwalanie(tab, n, i, j+1, cache)) + tab[i][j]


def falisz (T):
    n = len(T)
    cache = [[None for _ in range(n)] for x in range(n)]
    odp = uwalanie(T, n, n-1, n-1, cache)
    return odp


runtests ( falisz )
