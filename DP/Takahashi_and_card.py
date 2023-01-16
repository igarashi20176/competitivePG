N, A = map(int, input().split())
x = list(map(int, input().split()))
s = sum(x)

dp = [ [ [0 for _ in range(2600)] for _ in range(N+1) ] for _ in range(N+1) ]
dp[0][0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(s+1):
            # if k+x[i] >= 2500: continue
            dp[i+1][j][k] += dp[i][j][k]
            dp[i+1][j+1][k+x[i]] += dp[i][j][k]

ans = 0
for j in range(1, N+1):
    ans += dp[N][j][j*A] 

print(ans)


