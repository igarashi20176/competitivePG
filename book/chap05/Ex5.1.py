print("夏休みの日数は？")
N = input('>> ')
N = int(N)

# 3日間のそれぞれの幸福度
a = [[ int(input('>>')) for j in range(3)] for i in range(N) ]
        
# 0~3日目までだからN+1 (0は初期化されている必要がある...動的計画法はi-1が一意に決まっている必要あり)
dp = [[ 0 for j in range(3) ] for i in range(N+1) ]


def chmax(a, b):
    return a if a > b else b

for i in range(N):
    # i 日目の状態は j、i+1 日目の状態は k
    for j in range(3):
        for k in range(3):
            if k == j:
                continue
            dp[i+1][k] = chmax(dp[i+1][k], dp[i][j] + a[i][k])


# 最終日の最大値の選出
res = 0
for i in range(3):
    res = chmax(res, dp[N][i])

print(res)
print(dp)




