N = int(input())
H = list(map(int, input().split()))

INF = 10**8
dp = [INF for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    if i-2 >= 0:
        dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))
    else:
        dp[i] = dp[i-1] + abs(H[i]-H[i-1])

print(dp[N-1])