from zad6ktesty import runtests 


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


runtests ( haslo )