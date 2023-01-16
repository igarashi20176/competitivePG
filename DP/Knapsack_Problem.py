N, W = map(int, input().split())

value = []
weight = []
for i in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [ [0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if w >= weight[i]:
            dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i]] + value[i])
        else:
            dp[i+1][w] = dp[i][w]

print(dp[N][W])
    
