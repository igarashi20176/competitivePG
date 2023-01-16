N = int(input())

a = [ int(i) for i in input().split() ]

b = sorted(a, reverse=True)

Alice = 0
Bob = 0
for i in range(N):
    if i % 2:
        Bob += b[i]
    else:
        Alice += b[i]

print(Alice - Bob)