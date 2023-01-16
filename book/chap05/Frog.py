h = [ 2, 9, 4, 5, 1, 6, 10 ]

dp = [0] * len(h)

for i in range(1, len(h)):
    if i == 1:
        dp[i] = abs(h[i] - h[i-1])
    else:
        dp[i] = min( 
            dp[i-1] + abs(h[i] - h[i-1]),
            dp[i-2] + abs(h[i] - h[i-2]) 
        )

print(dp)
print(f'最小コスト: {dp[len(h)-1]}')