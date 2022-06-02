"""
Polecenie:
Zadanie offline 3.
Szablon rozwiązania: zad3.py
Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego.
Rozkład ten mamy zadany jako k przedziałów [a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z
prawdopodobieństwem ci
, a liczba z przedziału (x ∈ [ai, bi]) jest losowana zgodnie z rozkładem jednostajnym.
Przedziały mogą na siebie nachodzić. Liczby ai , bi są liczbami naturalnymi ze zbioru {1, . . . , N}.
Proszę zaimplementować funkcję SortTab(T, P) sortująca podaną tablicę i zwracająca posortowaną tablicę jako wynik.
Pierwszy argument to tablica do posortowania a drugi to opis przedziałów w postaci:
P = [(a_1,b_1,c_1), (a_2,b_2,c_2), ..., (a_k,b_k,c_k)]}.
Na przykład dla wejścia:
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P = [(1, 5, 0.75) , (4, 8, 0.25)]
po wywołaniu SortTab(T,P) tablica zwrócona w wyniku powinna mieć postaci:
T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
zaproponowanego algorytmu.

Opis działania programu:
Algorytm korzysta tylko i wyłącznie z tabeli z danymi. Algorytm zaczyna od stworzenia kubełków od 1 do N (możliwe
wartości) // 10, co znacznie zmniejsza liczbę kubełków do posortowania i zbadania. Nastepnie jeżeli kubełek posiada
tylko jeden element, to dodaje go do tablicy wynikowej. Jeśli jest mniej niż 15 elementów, to stosuję algorytm
InsertionSort, który działa dobrze na małych tablicah. Dla większych tablic (>15 elementów) stosuję algorytm QuickSort.

Złożoność oszacowałvym na O(n + logn)
"""

# from zad3testy import runtests


def quick_sort(tab, p, k):      # quicksort na podstawie wykładu
    if p < k:
        q = partition(tab, p, k)
        quick_sort(tab, p, q-1)
        quick_sort(tab, q+1, k)


def partition(tab, p, k):       # partition na podstawie wykładu
    x = tab[k]
    i = p-1
    rowne = p-1
    for j in range(p, k):
        if tab[j] < x:
            i += 1
            rowne += 1
            tab[i], tab[j] = tab[j], tab[i]

        elif tab[j] == x:
            rowne += 1
            tab[rowne], tab[j] = tab[j], tab[rowne]

    tab[i+1], tab[k] = tab[k], tab[i+1]
    return i+1


def SortTab(T,P):
    n = len(T)
    kubki = [[] for _ in range((n-1)//10)]      # Tworzymy n/10 kubełków
    for i in T:                                 # Przypisujemy odpowiednie wartości do ich kubełków
        kubki[(int(i) % n)//10].append(i)

    wynik = [0 for _ in range(n)]
    koniec = 0
    for i in range((n-1)//10):
        wielKub = len(kubki[i])
        if wielKub == 0:                        # dla pustego kubełka przechodzimy dalej
            continue

        elif wielKub == 1:                      # jesli jest jeden element, to go dodajemy do wynikowej tablicy
            wynik[koniec] = kubki[i][0]
            koniec += 1

        elif wielKub < 15:                      # jeśli jest mniej niż 15 elementów, stosujemy InsertionSort
            for k in range(1, wielKub):
                val = kubki[i][k]
                j = k - 1
                while j >= 0 and val < kubki[i][j]:
                    kubki[i][j + 1], kubki[i][j] = kubki[i][j], kubki[i][j + 1]
                    j -= 1

            for i in kubki[i]:
                wynik[koniec] = i
                koniec += 1

        else:                                   # Dla większych tablic robimy QuickSort
            quick_sort(kubki[i], 0, wielKub-1)

            for i in kubki[i]:
                wynik[koniec] = i
                koniec += 1

    return wynik


# runtests( SortTab )