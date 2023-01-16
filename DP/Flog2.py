N, K = map(int, input().split())
h = list(map(int, input().split()))
INF = 10**8

dp = [INF for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    dp[i] = dp[i-1] + abs(h[i-1] - h[i])

    for j in range(2, K+1):
        if i - j < 0 : continue

        dp[i] = min(dp[i], dp[i-j] + abs(h[i-j] - h[i]))

print(dp[N-1])