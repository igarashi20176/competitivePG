from collections import deque

dx = [ 1, 0, -1, 0 ]
dy = [ 0, 1, 0, -1 ]

H, W = map(int, input().split())

field = []
for _ in range(H):
    field.append(list(input()))


b_cnt = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == "#":
            b_cnt+=1


dist = [ [-1 for _ in range(W)] for _ in range(H) ]
dist[0][0] = 1

prev_y = [ [-1 for _ in range(W)] for _ in range(H) ]
prev_x = [ [-1 for _ in range(W)] for _ in range(H) ]

que = deque()
que.append((0, 0))

while(len(que)):
    v = que.popleft()
    y = v[0]
    x = v[1]
    
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (0 <= ny < H and 0 <= nx < W): continue
        if field[ny][nx] == "#": continue

        if dist[ny][nx] != -1: continue
        que.append((ny, nx))
        dist[ny][nx] = dist[y][x] + 1

        prev_y[ny][nx] = y
        prev_x[ny][nx] = x


print(H * W - dist[H-1][W-1] - b_cnt )

        







