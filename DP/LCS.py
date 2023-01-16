S = input()
T = input()

sl = len(S)
tl = len(T)

dp = [[0 for _ in range(tl+1)] for _ in range(sl+1)]
for i in range(sl):
    for j in range(tl):
        if S[i] == T[j]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])

lcs = ""
i = sl
j = tl
while i >= 0 and j >= 0:
    if S[i-1] == T[j-1]:
        lcs += S[i-1]
        i-=1
        j-=1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1 

print(lcs[::-1])

