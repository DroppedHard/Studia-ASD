# from zad4ktesty import runtests
"""
Zadanie 4 - Ścieżka Falisza
Szablon rozwiązania: zad4k.py
Dana jest mapa wyrażona poprzez tablicę dwuwymiarową wymiarów N x N zawierająca liczby naturalne. Król Falisz znajduje się na polu (0,0) tej tablicy. Jego celem jest dojście do pola (n-1, n-1) i w trakcie tego procesu oblanie jak najmniejszej liczby studentów (każde pole tablicy wyraża ilość studentów, która zostanie oblana, gdy król przejdzie przez to pole). Ze względu na regulamin studiów Falisz może poruszać się jedynie o 1 pole w prawo lub w dół. Proszę napisać algorytm, który określi jaka jest minimalna liczba studentów, która zostanie oblana aby król doszedł do celu. Dla ułatwienia zadania pola (0, 0) oraz (n-1, n-1) przyjmują stałą wartość 0.
Algorytm należy zaimplementować jako funkcję postaci:
def falisz( T ): …
która przyjmuje dwuwymiarową tablicę liczb naturalnych T i zwraca liczbę będącą minimalną ilością studentów, których król musi oblać.
Przykład. Dla tablicy:
T = [ [0, 5, 4, 3], [2, 1, 3, 2], [8, 2, 5, 1], [4, 3, 2, 0] ]
Wynikiem jest liczba 9
"""

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


# runtests ( falisz )
