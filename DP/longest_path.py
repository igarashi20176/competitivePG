def dp(v):
    if seen[v]: return memo[v]

    # 複数の経路において最短の経路を求める
    # ans = max()
    ans = 0
    for to in G[v]:
        ans = max(ans, dp(to) + 1)
    
    # 全ての経路を探索し終えたらTrue & memoに記録
    # memoにより同じパスを通ることが無く経路数をO(1)で取得可
    seen[v] = True
    memo[v] = ans
    return ans


N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())

    G[x-1].append(y-1)


seen = [False] * N
memo = [0] * N
ans = 0
for v in range(N):
    ans = max(ans, dp(v))

print(ans)