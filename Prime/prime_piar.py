N = int(input())

def hurui():
    isprime = [True] * (N+1)
    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        if not(isprime[p]):
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q+=p

    return isprime


res = 0
isprime = hurui()
for i in range(1, N, 2):
    if isprime[i] and isprime[i-2]:
        res+=1

print(res)
