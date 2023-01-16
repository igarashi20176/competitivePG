from itertools import permutations
import math

N = int(input())

dist = []
for i in range(N):
    x, y = map(int, input().split())

    dist.append((x, y))

per = permutations([i for i in range(N)])

ans = 0
cnt = 0
for p in per:
    cnt+=1
    res = 0
    for i in range(1, N):
        x1, y1 = dist[p[i]]
        x2, y2 = dist[p[i-1]]
        r = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
        res+=r

    ans+=res

print(ans / cnt)


    