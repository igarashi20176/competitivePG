n = 6
W = 9
weight = [2,1,3,2,1,5]
value = [3,2,6,1,3,85]
res = 0

# Wは0~W(Wを含む)までだからW+1, nは商品の数
# iは何個の商品を選ぶかだから0~n(nを含む)よってn+1
dp = [[0 for j in range(W+1)] for i in range(n+1)]

def chmax(a, b):
    return b if a < b else a

# i=0　何も選ばない状態
for i in range(n):
    # wは何kgの制限があるのか
    for w in range(W+1):
        # 選ぶ
        if w - weight[i] >= 0:
            res = chmax(dp[i+1][w], dp[i][w-weight[i]] + value[i])
            dp[i+1][w] = res

        # 選ばない
        res = chmax(dp[i+1][w], dp[i][w])
        dp[i+1][w] = res


for i in range(n+1):
    print(dp[i])
