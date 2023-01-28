def dfs(v):
    seen[v] = True
    
    for nv in G[v]:
        if seen[nv]: continue
        dfs(nv)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    t1, t2 = map(int, input().split())
    G[t1-1].append(t2-1)
    G[t2-1].append(t1-1)


res = 0
seen = [False for _ in range(N)]
for v in range(N):
    if not seen[v]: 
        res += 1
        dfs(v)

print(res)
