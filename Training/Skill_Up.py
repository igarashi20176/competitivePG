INF = 1 << 60

def judge(bit):
    C = 0
    A = [0] * m
    
    for i in range(n):
        if not(( bit >> i ) & 1):
            continue
        C += c[i]
        for j in range(m):
            A[j] += a[i][j]
        
    for i in range(m):
        if A[i] < x:
            return INF

    return C
            

n, m, x = map(int, input().split())
c = [0] * n
a = [[] for _ in range(n)]

for i in range(n):
    c[i], *a[i] = map(int, input().split())


ans = INF
for bit in range(2**n):
    ans = min(ans, judge(bit))
    
print("-1") if ans == INF else print(ans)