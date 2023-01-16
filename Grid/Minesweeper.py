H, W = [int(i) for i in input().split()]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

grid = []
for i in range(H):
    grid.append(list(input()))

for y in range(H):
    for x in range(W):

        if grid[y][x] == "#": continue

        grid[y][x] = 0

        for d in range(8):
            ix = x + dx[d]
            iy = y + dy[d]
            
            if ( 0 <= ix < W ) and (0 <= iy < H ):
                if grid[iy][ix] == "#":
                    grid[y][x] += 1            

for y in grid:
    print("".join(list(map(str, y))))
