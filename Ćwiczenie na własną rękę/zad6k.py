# from zad6ktesty import runtests 
"""
Zadanie 6 - Hasło do laptopa
Szablon rozwiązania: zad6k.py
Podczas Twoich praktyk zawodowych w biurze śledczym otrzymałeś zadanie dostania się do pewnego zabezpieczonego hasłem laptopa. Jedyną podpowiedzią jaką zostawił przestępca był pewien ciąg cyfr wyrażony jako string S. Odkryto już, że w rzeczywistości podpowiedź pozostawiona przez przestępcę była pewną tajną wiadomością, która została zakodowana poprzez zamienienie liter na znaki (tak np. A = 1, B = 2, …, Z = 26) oraz, że hasło ustawione przez przestępcę to tak naprawdę liczba wyrażająca całkowitą liczbę różnych wiadomości, które mogą ukrywać się pod zakodowanym ciągiem. Twoim zadaniem jest napisanie algorytmu, który zwróci poprawne hasło niezbędne do zalogowania się do laptopa. Możesz przyjąć, że pusty ciąg ma tylko 1 rozwiązanie, a niepoprawne wiadomości 0 rozwiązań (przez niepoprawne można uznać np. takie, które posiadają dwa zera pod rząd, z których nie da się odczytać żadnej litery)
Algorytm należy zaimplementować jako funkcję postaci:
def haslo( S ): …
która przyjmuje string S i zwraca liczbę będącą poprawnym hasłem do laptopa.
Przykład. Dla ciągu znaków:
S = "123"
Wynikiem jest liczba 3 ponieważ zaszyfrowana wiadomość "123" może zostać zakodowane jako "ABC" (123), "LC" (12 3) lub "AW" (1 23).
"""


def haslo (S):
    if "0" == S[0] or "00" in S:
        return 0
    else:
        n = len(S)
        cache = [0 for _ in range(n)]
        cache[0] = 1
        if S[1] == "0" and int(S[0]) > 2:
            return 0
        elif (S[1] == "0" and int(S[0]) <= 2) or (int(S[0])>2 or (int(S[0]) == 2 and int(S[1]) >= 7)):
            cache[1] = 1
        else:
            cache[1] = 2

        for i in range(2, n):
            if S[i] == "0" and int(S[i-1]) <= 2:     # nie ma dwóch 0 obok siebie
                cache[i] = cache[i - 2]

            elif S[i] == "0" and int(S[i-1]) >2:
                return 0

            elif S[i-1] == "0" or int(S[i-1]) >= 3 or (S[i-1] == "2" and int(S[i]) >= 7):
                cache[i] = cache[i-1]
            else:
                cache[i] = cache[i-1] + cache[i-2]

        print(S)
        print(cache)
        return cache[n-1]


# runtests ( haslo )
