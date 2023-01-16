W = int(input())
N, K = map(int, input().split())


width = []
value = []
for i in range(N):
    a, b = map(int, input().split())

    width.append(a)
    value.append(b)

dp = [[[0 for _ in range(K+1)] for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        for k in range(K):
            if w-width[i] >= 0:
                dp[i+1][w][k+1] = max(dp[i][w-width[i]][k] + value[i], dp[i][w][k])
            else:
                dp[i+1][w][k] = dp[i][w][k]

ans = 0
for w in range(W+1):
    for k in range(K+1):
        ans = max(ans, dp[N][w][k])

print(ans)



            

            

