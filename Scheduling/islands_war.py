N, M = map(int, input().split())

long = []
for i in range(M):
    a, b = map(int, input().split())

    long.append((a, b))
    
long.sort(key=lambda x: x[1])

curr_end = 0
res = 0
for i in range(M):
    if long[i][0] < curr_end: continue

    curr_end = long[i][1]
    res+=1
    
print(res)

    