"""
Zadanie 1 - Największa różnica w podciągu
Szablon rozwiązania: zad1k.py
Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego ciągu, w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w ciągu występują same jedynki, należy założyć, że rozwiązaniem jest -1
Algorytm należy zaimplementować jako funkcję postaci:
def roznica( S ): …
która przyjmuje ciąg S i zwraca wyliczoną największą osiągalną różnicę.
Przykład. Dla ciągu:
11000010001
Wynikiem jest liczba 6
"""

# from zad1ktesty import runtests


def roznica(S):
    print(S)
    n = len(S)
    wynik = [[0 for _ in range(x)] for x in range(n, -1 ,-1)]

    only1 = True
    roznica = 0
    for i in range(n):
        if S[i] == "0":
            only1 = False
            roznica += 1
        else:
            roznica -= 1

        wynik[0][i] = roznica

    if only1:
        return -1

    odp = 0
    for i in range(n-1):
        dozmiany = 0
        if S[i] == "0":
            dozmiany -= 1
        else:
            dozmiany += 1

        for j in range(n-i):
            wynik[i+1][j-1] = wynik[i][j] + dozmiany
            if odp < wynik[i][j] + dozmiany:
                odp = wynik[i][j] + dozmiany

    return odp

# runtests ( roznica )
