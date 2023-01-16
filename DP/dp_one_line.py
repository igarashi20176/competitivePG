N, W = map(int, input().split())

value = []
weight = []
for i in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [0 for _ in range(W+1)]

for i in range(N):
    for w in range(W+1):
        if w >= weight[i]:
            dp[w] = max(dp[w], dp[w-weight[i]] + value[i])

print(dp[-1])

