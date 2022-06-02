"""
Polecenie:
Zadanie offline 2.
Szablon rozwiązania: zad2.py
Dany jest ciąg przedziałów domkniętych L = [[a1, b1], . . . ,[an, bn]]. Początki i końce przedziałów
są liczbami naturalnymi. Poziomem przedziału c ∈ L nazywamy liczbę przedziałów w L, które w
całości zawierają się w c (nie licząc samego c). Proszę zaproponować i zaimplementować algorytm,
który zwraca maksimum z poziomów przedziałów znajdujących się w L. Proszę uzasadnić poprawność algorytmu i
oszacować jego złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję postaci:
def depth( L ):
...
która przyjmuje listę przedziałów L i zwraca maksimum z poziomów przedziałów w L.
Przykład. Dla listy przedziałów:
L = [ [1, 6],
[5, 6],
[2, 5],
[8, 9],
[1, 6]]
wynikiem jest liczba 3

Opis programu:
Program działa na bazie quicksorta, sortującego tablicę po pierwszym elemencie tablicy.
Po posortuwaniu dwie pętle while sprawdzają warunki zawierania się przedziałów.
Do tego dodane są warunki kończące pętle, dzięki czemu program działa szybciej.
Nie jest to wystarczające do wszystkich testów, ale trochę usprawnia program :)
1 warunek opiera się na znalezionym poziomie przedziału (maxc) -
        n-i-1 > maxc
Przy niespełnieniu tego warunku, dalsze sprawdzanie nie ma sensu, ponieważ od pewnego i nie znajdziemy
tylu przedziałów, by "pobiło" nasze do tej pory znalezione maxc. Ten warunek zawszięczamy posortowaniu tablicy.

2 warunek opiera się na badaniu granicy lewej następnego przedziału i granicy prawej przedziału badanego.
Jeśli przedziały się wykluczają, to nie spełniaja warunków zadania, więc można zakończyć dalsze szukanie.

3 warunek opiera się na zmiennej "rowne", która pomaga nie pominąć początkowych elementów o takiej samej granicy
lewostronnej.

Algorytm niestety ma złożoność O(nlogn + n^2) - nlogn - quicksort, n^2 pętla licząca wliczające się podzbiory.
Są ograniczenia, jednak nie jest to wystarczające.
"""

# from zad2testy import runtests


def quick_sort(tab, p, k):      # quicksort na podstawie wykładu
    if p < k:
        q = partition(tab, p, k)
        quick_sort(tab, p, q-1)
        quick_sort(tab, q+1, k)


def partition(tab, p, k):       # partition na podstawie wykładu
    x = tab[k][0]
    i = p-1
    rowne = p-1
    for j in range(p, k):
        if tab[j][0] < x:
            i += 1
            rowne += 1
            tab[i], tab[j] = tab[j], tab[i]
        elif tab[j][0] == x:
            rowne += 1
            tab[rowne], tab[j] = tab[j], tab[rowne]
    tab[i+1], tab[k] = tab[k], tab[i+1]

    return i+1


def depth(L):
    n = len(L)
    quick_sort(L, 0, n-1)

    maxc = 0
    rowny = 0
    i = 0
    while i < n and n - i - 1 > maxc:       # warunek 1, wyżej opisany
        c = 0
        if L[rowny][0] != L[i][0]:  # warunek 3, tutaj sprawdzamy czy mamy element o innej lewej granicy
            rowny = i

        j = rowny
        while j < n and L[i][1] > L[j][0]:      # warunek 2 kończy naszą pętlę wewnętrzną
            if i == j:
                j += 1
                continue

            if L[i][0] <= L[j][0] and L[i][1] >= L[j][1]:     # sprawdzamy czy znaleźliśmy element spełniający założenia
                c += 1

            j += 1

        if c > maxc:
            maxc = c

        i += 1

    return maxc


# runtests( depth )
