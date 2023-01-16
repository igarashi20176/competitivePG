# 要素の数
N = int(input('N: '))
# 総和がWに一致するか
W = int(input('W: '))

a = [ int(input(f'数字{i+1}: ')) for i in range(N) ]


dp = [ [False for j in range(W+1)] for i in range(N+1) ]
# 初期値
dp[0][0] = True


for i in range(N):
    for j in range(W+1):
        # 選ばない場合
        # つまり，Trueの状態(まだ総和に達していない)を引き継ぐ
        if dp[i][j]:
            print('----------------------')
            print(i, j)
            dp[i+1][j] = True
        
        # 選ぶ場合
        # j >= a[i]... 配列のindexがマイナスにならない為の条件
        # dp[i][j - a[i]]... 値を足す前の値がまだ総和に達していない場合
        if j >= a[i] and dp[i][j - a[i]]:
            print(i, j)
            dp[i+1][j] = True


for i in range(N+1):
    print(dp[i])
print("yes" if dp[N][W] else "no")

    
