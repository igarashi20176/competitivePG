N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
V_MAX = 100001
INF = 2 * 10**9

dp = [ [INF for _ in range(V_MAX) ] for _ in range(N+1) ]
dp[0][0] = 0

for i in range(N):
    for j in range(V_MAX):
        if (dp[i][j] == INF): continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        if (dp[i][j] + wv[i][0] > W): continue 
        dp[i+1][j+wv[i][1]] = min(dp[i+1][j+wv[i][1]], dp[i][j] + wv[i][0])


res = 0
for j in range(V_MAX-1, 0, -1):
   if dp[N][j] <= W:
        res = j
        break

print(res)


        

