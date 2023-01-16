W, H = map(int, input().split())

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

field = []
for i in range(H):
    field.append(list(map(int, input().split())))


def dfs(h, w):
    field[h][w] = 0

    for i in range(8):
        xx = w + dx[i]
        yy = h + dy[i]

        if 0 <= xx < w and 0 <= yy < h: continue
        if field[yy][xx] == 0: continue
        dfs(yy, xx)

count = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == 0: continue
        dfs(i, j)
        count+=1

print(count)