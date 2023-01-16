from itertools import product

N, M = map(int, input().split())

S = [[] for _ in range(N)]

for i in range(M):
    k, *s = map(int, input().split())

    for j in s:
        S[j-1].append(i)

P = list(map(int, input().split()))

ans = 0
def f(bit):
    cnt = [0] * M
    for i in range(N):
        if not bit[i]:
            continue
            
        for j in S[i]:
                cnt[j]+=1

    for c, p in zip(cnt, P):
        if c % 2 != p:
            return False
    
    return True

for bit in product(range(2), repeat=N):
    ans += f(bit)

print(ans)
            

        
    