from collections import deque

dx = [ 1, 0, -1, 0 ]
dy = [ 0, 1, 0, -1 ]

H, W = map(int, input().split())

field = []
for _ in range(H):
    field.append(list(input()))


sh, sw, gh, gw = [0,0,0,0]
b_cnt = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == "S":
            sh = i
            sw = j
        if field[i][j] == "G":
            gh = i
            gw = j
        if field[i][j] == "#":
            b_cnt+=1


dist = [ [-1 for _ in range(W)] for _ in range(H) ]
dist[sh][sw] = 0

prev_y = [ [-1 for _ in range(W)] for _ in range(H) ]
prev_x = [ [-1 for _ in range(W)] for _ in range(H) ]

que = deque()
que.append((sh, sw))

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


y = gh
x = gw
while x != -1 and y != -1:
    field[y][x] = "o"
    
    x = prev_x[y][x]
    y = prev_y[y][x]

    
for i in range(H):
    print("".join(field[i]))
        







