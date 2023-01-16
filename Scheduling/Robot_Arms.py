N = int(input())

long = []
for i in range(N):
    x, l = map(int, input().split())
    
    long.append((x-l, x+l))

long.sort(key=lambda x: x[1])
    
curr_end = -10*10
res = 0
for i in range(N):
    if long[i][0] < curr_end: continue

    res+=1
    curr_end = long[i][1]

print(res)