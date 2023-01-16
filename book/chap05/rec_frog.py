# 最小化問題のため基準値となるresは極大値にする
res = 10000

h = [ 2, 9, 4, 5, 1, 6, 10 ]
len_h = len(h)
dp = [res] * len_h
dp[0] = 0


def chmin(res, c):
    if res > c:
        res = c
    return res

def rec(i):
    res = 10000

    if dp[i] < res:
        return dp[i]

    if i == 0:
        return 0

    res =  chmin(res, rec(i-1) + abs(h[i] - h[i-1]))

    if i > 1:
        res = chmin(res, rec(i-2) + abs(h[i] - h[i-2]))

    dp[i] = res

    return res


rec(len_h-1)

print(dp)
    
    
    