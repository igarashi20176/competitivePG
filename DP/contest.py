N = int(input())
A = list(map(int, input().split()))

W = N*100
dp = [[False for _ in range(W+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for w in range(W+1):
        if not dp[i][w]: continue

        dp[i+1][w] = True

        if w+A[i] <= W:
            dp[i+1][w+A[i]] = True


ans = 0
for i in range(W+1):
    if dp[N][i]: ans+=1

print(ans)
