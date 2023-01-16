N = int(input())
S = list(input())

E = [0 for _ in range(N)]
W = [0 for _ in range(N)]

for i in range(N):
    if S[i] == "W":
        W[i] = 1
    else:
        E[i] = 1

for i in range(1, N):
    W[i] += W[i-1]
    E[i] += E[i-1]

ans = 10**6
for i in range(N):
    res = 0
    if i:
        res += W[i-1]
    res += E[N-1] - E[i]

    ans = min(ans, res)

print(ans)