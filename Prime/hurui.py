N = 100

def hurui():
    isprime = [True] * (N+1)
    isprime[0], isprime[1] = False, False

    for i in [2, 3, 5]:
        if not(isprime[i]):
            continue

        q = i * 2
        while q <= N:
            isprime[q] = False
            q+=i

    return isprime

    
print(hurui().count(True))
