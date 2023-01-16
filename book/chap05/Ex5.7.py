s = input('S: ')
t = input('T: ')

N = len(s)
M = len(t)

dp  = [[0 for j in range(M+1)] for i in range(N+1)]

def chmax(a, b):
    return a if a > b else b

for i in range(N+1):
    for j in range(M+1):
        if i > 0 and j > 0:
            if s[i-1] == t[j-1]:
                dp[i][j] = chmax(dp[i][j], dp[i-1][j-1] + 1)
            else:
                dp[i][j] = chmax(dp[i][j], dp[i-1][j-1])

            if i > 0:
                dp[i][j] = chmax(dp[i][j], dp[i-1][j])

            if j > 0:
                dp[i][j] = chmax(dp[i][j], dp[i][j-1])

for i in range(N+1):
    print(dp[i])
print(dp[N][M])