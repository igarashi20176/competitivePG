import math

N, T = map(int, input().split())
A = list(map(int, input().split()))

rest = T % sum(A)

sum = 0
for i in range(N):
    if sum + A[i] > rest:
        print(i + 1, rest - sum)
        break
    sum += A[i]



