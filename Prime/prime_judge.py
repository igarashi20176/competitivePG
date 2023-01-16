def isPrime(N):
    if N < 2:
        return False

    i = 2
    while i*i <= N:
        if N % i == 0:
            return False
        i+=1

    return True


N = int(input())
res = 0
for i in range(2, N+1):
    if isPrime(i) and isPrime(N-i):
        res = i
        break

print(res)
