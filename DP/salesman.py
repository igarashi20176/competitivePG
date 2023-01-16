def rec(bit, v):
    if dp[bit][v] != -1:
        return dp[bit][v]

    if bit == (1<<v):
        dp[bit][v] = 0
        return dp[bit][v]

    res = INF
    prev_bit = bit & ~(1<<v)

    for u in range(N):
        if not( prev_bit & (1<<u) ): continue

        if res > rec(prev_bit, u) + dist[u][v]:
            res = rec(prev_bit, u) + dist[u][v]

    dp[bit][v] = res
    return dp[bit][v]


INF = 100000000
N = int(input())

tmp = []
for i in range(N):
    tmp.append(list(map(int, input().split())))


dist = [[0 for _ in range(21)] for _ in range(21)]
for i in range(N):
    for j in range(N):
        dist[i][j] = tmp[i][j]

dp = [[-1 for _ in range(N)] for _ in range(1<<N)]

res = INF
for v in range(N):
    if res > rec((1<<N)-1, v):
        res = rec((1<<N)-1, v)

for i in range(2**N):
    print(dp[i])