MOD = 10**9+7

def add(x, y):
    sum = x + y
    if sum >= MOD:
        return sum % MOD

    return sum


H, W = map(int, input().split())
grid = [ list(input()) for _ in range(H) ]

dp = [ [0] * (W) for _ in range(H) ]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i+1 < H and grid[i+1][j] == ".":
            dp[i+1][j] = add(dp[i+1][j], dp[i][j])
        if j+1 < W and grid[i][j+1] == ".":
            dp[i][j+1] = add(dp[i][j+1], dp[i][j])
        
print(dp[H-1][W-1])
            

