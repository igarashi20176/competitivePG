H, W = map(int, input().split())

# dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

seen = [[False for _ in range(500)] for _ in range(500)]
def dfs(h, w):
    seen[h][w] = True
    
    for i in range(4):
        xx = w + dx[i]
        yy = h + dy[i]

        if 0 <= xx < W and 0 <= yy < H: continue
        if seen[yy][xx] == True: continue
        if field[yy][xx] == "#": continue

        dfs(yy, xx)


field = []
for i in range(H):
    field.append(list(input()))

sh, sw, gh, gw = [0,0,0,0]
for i in range(H):
    for j in range(W):
        if field[i][j] == "s":
            sh = i
            sw = j
        if field[i][j] == "g":
            gh = i
            gw = j

dfs(sh, sw)

print("Yes") if seen[gh][gw] else print("No")
