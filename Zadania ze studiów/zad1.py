"""
Polecenie:
Zadanie offline 1.
Szablon rozwiązania: zad1.py
Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
def __init__(self):
self.val = None # przechowywana liczba rzeczywista
self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an
(lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu
listy znalazłby się na pozycji różniącej się od bieżącejo najwyżej k.
Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n listy
oraz parametru k). Proszę skomentować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
k = Θ(n).

Opis algorytmu:
Zadanie offline z ASD - Pierwszy tydzień
Program polega na zastosowaniu algorytmu BubbleSort z pewnymi ulepszeniami dla k=1,
a dla k>1 zastosowanie algorytmu HeapSort.
Obok każdej funkcji zamieszczam wyjaśnienie, co ma robić, a przy obszerniejszych częściach opis bardziej znaczących
części kodu.

Działanie dla k=1:
Korzystam z bubble sort, ponieważ wtedy elementy są albo obok swoich pozycji, albo są na miejscu.
Dzięki temu jedna iteracja bubble sorta wystarczy by posortować dane.
Działanie - sprawdzam 2 kolejne wartości. Jeśli są ułożoone malejąco, to zamieniam je miejscami i iteruję o 2 pozycje.
Jeśli wartości są rosnąco, to przechodzę o jedną pozycję dalej.

Dla k>1:
Wykorzystałem HeapSort - tworzę tablicę o długości k+1. Do niej dodaję pierwsze k+1 elementów z listy odsyłaczowej.
Potem tworzę kopiec (drzewo binarne), gdzie rodzicem jest wartość mniejsza od dzieci (odwrotnie niż na wykładzie)
Dzięki temu znajduję najmniejszy element z k+1 potencjalnych elementów.
Znaleziony element dołączam do wynikowej listy odsyłaczowej, po czym usuwam dodany element i dodaję kolejny
z początkowej listy odsyłaczowej.
Jeśli dojdę do końca początkowej listy odsyłaczowej, to wykonuję ww. operację za każdym razem skracając długość listy.

Złożoność czasowa dla:
k = Θ(1):       Wtedy jest lniowa: Θ(n)
k = Θ(log(n)):  Wtedy złożoność to Θ(n*(log(log(n))))
k = Θ(n):       Wtedy złożoność to Θ(n*(log(n)))
"""

# from zad1testy import Node, runtests


def heapify(tab, n, i):     # funkcja "naprawiająca" n elementów kopca podanego za pomocą zmiennej tab. (z wykładu)
    left = 2*i + 1             # z małą zmianą, dzięki której pierwszym elementem jest element najmniejszy
    right = 2*i + 2             # left i right - przechowująindeks lewego i prawego dzieca elementu o i-tym indeksie
    min = i
    if left < n and tab[left].val < tab[min].val:
        min = left
    if right < n and tab[right].val < tab[min].val:
        min = right
    if min != i:
        tab[i], tab[min] = tab[min], tab[i]
        heapify(tab, n, min)


def buildHeap(tab):         # funkcja budująca kopiec dla elementów podanych w tablicy tab
    n = len(tab)
    for i in range((n-2)//2, -1, -1):
        heapify(tab, n, i)


def bubblesort(p):          # ulepszony bubblesort dla k=1.
    start = p           # start - wskaźnik, który jest pierwszym elementem listy wynikowej
    before = None       # before.next i now.next będą przechowywały node-y, które będziemy sprawdzać.
    now = p
    if p.val > p.next.val:      # pierwsze sprawdzanie, by odpowiedni wskaźnik początkowy start został zapisany.
        start = p.next
        start.next, p.next = p, start.next
        before = start.next
        now = before.next
    else:
        before = start
        now = before.next

    while now.next is not None:     # główna pętla iterująca przez całą listę i zamieniająca odpowiednio elementy.
        if before.next.val > now.next.val:
            before.next = now.next
            tmp = now.next
            now.next = now.next.next
            tmp.next = now
            before = before.next.next
            now = before.next
        else:       # przechodzimy co jeden element przy braku zmian, a co dwa przy zamianie.
            before = before.next
            now = before.next

    return start


def SortH(p,k):     # główna funkcja
    if k == 0:      # wtedy lista jest posortowana. Nie trzeba nic robić
        return p
    elif k == 1:    # tutaj wykonujemy ulepszony bubblesort
        return bubblesort(p)
    else:           # dla k>1 stosujemy HeapSort
        toadd = p    # toadd - element z początkowej listy odsyłaczowej do dodania w kolejnej iteracji.
        tab = [p]
        for i in range(k):  # Tworzymy tablicę długości k+1 z początkowymi elementami zadanej listy odsyłaczowej.
            if toadd.next is not None:
                toadd = toadd.next
                tab.append(toadd)
            else:
                break

        buildHeap(tab)      # Z tej tablicy tworzymy kopiec, którego pierwszy element jest najmniejszy
        start = tab[0]
        tail = start        # tail - ostatni element wynikowej listy odsyłaczowej. Do niego dodajemy kolejne elementy
        n = len(tab)        # posortowanej listy wynikowej.
        while toadd.next is not None:   # dopóki możemy dodać kolejny element do tablicy:
            toadd = toadd.next
            tab[0] = toadd  # dodajemy element do 0 indeksu tablicy
            heapify(tab, n, 0)  # naprawiamy kopiec po dodaniu elementu
            tail.next = tab[0]  # pierwszy element jest najmniejszy, dodajemy go do listy wynikowej
            tail = tail.next    # tail musi być ostatnim elementem wynikowej listy odsyłaczowej
            if toadd is not tail:   # ta cęść zapobiega powstawaniu cyklów w liście wynikowej
                tail.next = None

        while n > 0:    # dopóki sa elementy w tablicy
            buildHeap(tab)  # analogicznie jak wyżej, tylko za każdym razem tworzymy kopiec, ponieważ usunięcie
            n -= 1          # pierwszego elementu tworzy więcej niż jeden bład w nowej tablicy.
            tail.next = tab.pop(0)
            tail = tail.next
            tail.next = None

        return start        # zwracamy pierwszy wskaźnik z listy wynikowej.


# runtests( SortH )
