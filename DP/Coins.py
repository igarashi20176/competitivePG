N = int(input())
p = list(map(float, input().split()))

dp = [ [0] * (N+1) for i in range(N+1) ]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # i枚投げて，ちょうどj枚表だった確立 

        # 表の場合
        dp[i+1][j+1] += dp[i][j] * p[i]

        #ウラの場合
        dp[i+1][j] += dp[i][j] * (1-p[i])

ans = 0
# 枚数が表の方が多いとき
for i in range(N//2+1, N+1):
    ans += dp[N][i]

print(ans)