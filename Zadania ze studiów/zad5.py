"""
Polecenie:
Zadanie offline 5.
Szablon rozwiązania: zad5.py
W roku 2050 spokojny Maksymilian odbywa podróż przez pustynię z miasta A do miasta B.
Droga pomiędzy miastami jest linią prostą na której w pewnych miejscach znajdują się plamy ropy.
Maksymilian porusza się 24 kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy. Cysterna
wyposażona jest w pompę pozwalającą zbierać ropę z plam. Aby dojechać z miasta A do miasta
B Maksymilian będzie musiał zebrać ropę z niektórych plam (by nie zabrakło paliwa),
co każdorazowo wymaga zatrzymania cysterny. Niestety, droga jest niebezpieczna.
Maksymilian musi więc tak zaplanować trasę, by zatrzymać się jak najmniej razy.
Na szczęście cysterna Maksymiliana jest ogromna - po zatrzymaniu zawsze może zebrać całą ropę z plamy
(w cysternie zmieściłaby się cała ropa na trasie).
Zaproponuj i zaimplementuj algorytm wskazujący, w których miejscach trasy Maksymilian powinien się zatrzymać i zebrać ropę.
Algorytm powinien być możliwe jak najszybszy i zużywać jak najmniej pamięci.
Uzasadnij jego poprawność i oszacuj złożoność obliczeniową.
Dane wejściowe reprezentowane są jako tablica liczb naturalnych T,
w której wartość T[i] to objętość ropy na polu numer i (objętość 0 oznacza brak ropy). Pola mają numery od 0 do n − 1 a
odległość między kolejnymi polami to 1 kilometr. Miasto A znajduje się na polu 0 a miasto B na polu n − 1.
Zakładamy, że początkowo cysterna jest pusta, ale pole 0 jest częścią plamy ropy, którą
można zebrać przed wyruszeniem w drogę. Zakładamy również, że zadanie posiada rozwiązanie, t.j.
da się dojechać z miasta A do miasta B.
Algorytm należy zaimplementować w funkcji:
def plan(T):
...
która przyjmuje tablicę z opisem pół T[0], . . ., T[n-1] i zwraca listę pól, na których należy się
zatrzymać w celu zebrania ropy. Lista powinna być posortowana w kolejności postojów. Postój na
polu 0 również jest częścią rozwiązania.
Przykład. Dla wejścia:
# 0 1 2 3 4 5 6 7
T = [3,0,2,1,0,2,5,0]
wynikiem jest np. lista [0,2,5].

Opis programu:
Program korzysta z wbudowanej kolejki priorytetowej. Program zaczyna od pobrania dystansu, jaki możemy przejechać na
podstawie pierwszego postoju.Odpowiednio jest to dodawane do wyniku. Następnie wszystkie następne elementy dodajemy do
kolejki priorytetowej, dzięki czemu na pierwszym miejscu kolejki będzie opcja najlepsza w naszym zasięgu jazdy.

Dzięki odpowiedniemu dodawaniu elementów do kolejki priorytetowej otrzymujemy dokładnie to, czego potrzebujemy
(największy dystans poprzez pomnożenie dystansu przez -1, a indeks z tablicy T poprzez zapisanie go razem z ujemnym
dystansem w formie jednej krotki)

Program ma złożoność obliczeniową O(n) = nlogn, ponieważ dodawanie elementów do kolejki jest w trakcie logn.
Pamięciowa złożoność to O(n) = n, ponieważ n elementów dodamy do kolejki.
Pozdrawiam i chciałbym nie dostać plagiatu :)
Zrobiłem inną wersję, ale ta jest najszybsza.
"""
# from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    droga = len(T)
    dystans = T[0]
    opcje = PriorityQueue()
    wynik = [0]

    i = 1
    while dystans < droga-1:
        opcje.put(((-1) * T[i], i))
        if i == dystans:
            postoj = opcje.get()
            dystans -= postoj[0]
            wynik.append(postoj[1])

        i += 1

    wynik.sort()
    return wynik

# zmien all_tests na True zeby uruchomic wszystkie testy

# runtests( plan, all_tests = True )