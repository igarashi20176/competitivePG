N, W = map(int, input().split())

value = []
weight = []
for i in range(N):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)


dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(N):
    for w in range(W+1):
        if w - weight[i] >= 0:
            # 解説 https://qiita.com/drken/items/ace3142967c4f01d42e9#%E5%80%8B%E6%95%B0%E5%88%B6%E9%99%90%E3%81%AA%E3%81%97%E3%83%8A%E3%83%83%E3%83%97%E3%82%B5%E3%83%83%E3%82%AF
            # 個数制限有: 荷物iを選ぶ → dp[i+1]に遷移
            # 無: 荷物iを選んだdp[i+1]の状態から，さらに荷物iを選び遷移してくる可能性が
            # あるため，dp[i+1]の状態を再度max比較する
            dp[i+1][w] = max(dp[i][w], dp[i+1][w-weight[i]] + value[i])
        else:
            dp[i+1][w] = dp[i][w]

for i in range(N+1):
    print(dp[N])
