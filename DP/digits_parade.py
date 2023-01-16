S = input()
ls = len(S)
MOD = 10**9+7


def add(x, y):
    sum = x + y
    if sum >= MOD:
        sum = sum % MOD
    return sum

dp = [ [0 for _ in range(13)] for _ in range(ls+1) ]
dp[0][0] = 1

for i in range(ls):
    for j in range(13):
        if S[i] == "?":
            for k in range(10):
                dp[i+1][(j*10+k)%13] = add(dp[i+1][(j*10+k)%13], dp[i][j])
        else:
            k = int(S[i])
            dp[i+1][(j*10+k)%13] = add(dp[i+1][(j*10+k)%13], dp[i][j])

            

                
