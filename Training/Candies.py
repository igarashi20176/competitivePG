N = int(input())
A = []
dp = [[0 for j in range(N)] for i in range(2) ]

for i in range(2):
    A.append(list(map(int, input().split())))

dp[0][0] = A[0][0]
dp[1][0] = A[0][0] + A[1][0]


for i in range(1, N):
    dp[0][i] = dp[0][i-1] + A[0][i] 
    dp[1][i] = max(dp[0][i], dp[1][i-1]) + A[1][i] 

print(dp[1][N-1])


