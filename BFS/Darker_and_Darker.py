from collections import deque

q = deque()
dxy = [(0,1),(1,0),(0,-1),(-1,0)]

H, W = map(int,input().split())


grid = []
for _ in range(H):
    grid.append(list(input()))


dist = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            q.append((i, j))  
            dist[i][j] = 0

while len(q):
    v = q.popleft()
    y = v[0]
    x = v[1]

    for dx, dy in dxy:
        yy = y + dy
        xx = x + dx

        if 0 <= xx < W and 0 <= yy < H:
            if grid[yy][xx] == "#": continue
            if dist[yy][xx] != -1: continue

            q.append((yy, xx))
            dist[yy][xx] = dist[y][x] + 1

ans = -1
for i in range(H):
    for j in range(W):
        ans = max(ans, dist[i][j])

print(ans)



