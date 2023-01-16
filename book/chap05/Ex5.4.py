N = int(input('N: '))
# 総和がWに一致するか
W = int(input('W: '))

K = int(input("いくつ以下: "))

a = [int(input(f'数{i+1}: ')) for i in range(N)]
dp = [[10000 for j in range(W+1)] for i in range(N+1)]
dp[0][0] = 0

def chmin(a, b):
    return a if a < b else b


for i in range(N):
    for j in range(W+1):
        # 選ばない
        dp[i+1][j] = chmin(dp[i+1][j], dp[i][j])

        #　選ぶ
        if j >= a[i]:
            dp[i+1][j] = chmin(dp[i+1][j], dp[i][j-a[i]] + 1)


for i in range(N+1):
    print(dp[i])

print(f"yes { dp[N][W] }" if dp[N][W] <= K else "no")