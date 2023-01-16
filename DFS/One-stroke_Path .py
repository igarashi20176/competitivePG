def dfs(v):
    seen[v] = True

    ok = True
    for i in seen:
        if not(i): 
            ok = False
    
    if ok:
       res[0]+=1


    for i in G[v]:
        if seen[i]: continue
        dfs(i)
    
    seen[v] = False


N, M = map(int, input().split())

G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

seen = [False for i in range(N)]
res = [0]

dfs(0)

print(res[0])


