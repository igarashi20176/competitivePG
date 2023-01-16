H, W = [int(i) for i in input().split()]

grid = []
for y in range(H):
    grid.append(list(input()))


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0 ]

can = True
for y in range(H):
    for x in range(W):

        if grid[y][x] != "#": continue

        for d in range(4):
            yy = y + dy[d]
            xx = x + dx[d]

            if ( 0 <= xx < W ) and ( 0 <= yy < H ):
                if grid[yy][xx] != "#":
                    can = False
                else:
                    can = True
                    break
            
        if not(can):
            break
    else:
        continue
    break

print("Yes") if can else print("No")
                    