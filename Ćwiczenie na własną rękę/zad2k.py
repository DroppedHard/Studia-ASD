# from zad2ktesty import runtests

"""
Zadanie 2 - Najdłuższy palindrom
Szablon rozwiązania: zad2k.py
Dany jest ciąg liter S. Proszę znaleźć taki SPÓJNY fragment tego podciągu, który będzie najdłuższym możliwym palindromem.
Algorytm należy zaimplementować jako funkcję postaci:
def palindrom( S ): …
która przyjmuje ciąg S i zwraca ten najdłuższy palindrom.
Przykład. Dla ciągu:
aacaccabcc
Wynikiem jest ciąg acca
"""


# def czyPalindrom(str, p, dl, wyniki):
def czyPalindrom(str, p, dl,):
    # if dl < len(wyniki[p]) and wyniki[p][dl] is not None:
    #     return wyniki[p][dl]
    if dl < 0:
        return True
    if str[p] == str[p+dl]:
        # return czyPalindrom(str, p+1, dl-2, wyniki)
        return czyPalindrom(str, p+1, dl-2)
    else:
        return False


def palindrom(S):
    n = len(S)
    maks = ""
    # wyniki = [[None for _ in range(x)] for x in range(n, 0, -1)]
    for i in range(n):
        for j in range(n-i-1):
            # print(i, j)
            # if czyPalindrom(S, i, j, wyniki):
            if czyPalindrom(S, i, j):
                if len(maks) < j:
                    maks = S[i:i+j+1]
                    # print(S[i:j+1])
                # while j > 0:
                #     wyniki[i][j] = True
                #     i+=1
                #     j-=2

    return maks


# runtests ( palindrom )
