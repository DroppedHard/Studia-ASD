# from zad3ktesty import runtests
"""
Zadanie 3 - Najmniejsza k-ładna suma
Szablon rozwiązania: zad3k.py
Dla każdego ciągu n liczb możemy obliczyć k-ładną sumę (Zakładamy, że k <= n). Poprzez k-ładną sumę rozumiemy minimalną sumę pewnych liczb wybranych w ten sposób, że z każdych k kolejnych elementów wybraliśmy przynajmniej jeden z nich (w szczególności oznacza to, że dla k=1 musimy wybrać wszystkie elementy, a dla k=n wystarczy wybrać jeden, najmniejszy z nich). Proszę napisać algorytm, który dla zadanej tablicy liczb naturalnych oraz wartości k oblicza k-ładną sumę.
Algorytm należy zaimplementować jako funkcję postaci:
def ksuma( T, k ): …
która przyjmuje tablicę liczb naturalnych T = [a1, a2, …, an] oraz liczbę naturalną k.
Przykład. Dla tablicy:
[1, 2, 3, 4, 6, 15, 8, 7] oraz k = 4
Wynikiem jest liczba 7
"""

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


# runtests ( ksuma )
