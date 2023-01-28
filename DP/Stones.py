N, K = map(int, input().split())

a = list(map(int, input().split()))
dp = [False] * (K+1)


for k in range(K+1):
    for i in range(N):
        if k - a[i] < 0: continue

        dp[k] |= not dp[k-a[i]]

print("First") if dp[K] else print("Second")
            
