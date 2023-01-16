N, M = map(int, input().split())

C = list(map(int, input().split()))
INF = 10*6

dp = [INF] * (N+1)
dp[0] = 0
for c in C:
    for i in range(N+1):
        if i + c > N: break
        if dp[i] != INF:
            dp[i+c] = min(dp[i+c], dp[i]+1)

print(dp[-1])
            
        
        
