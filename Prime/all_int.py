import math

N, M = map(int, input().split())

def factorial(n):
    ans = []
    tmp = n
    p = 2
    while p * p <= n:
        res = 0
        while True:
            if tmp % p: break

            tmp//=p
            res+=1

        if res: ans.append((p, res))
        p+=1
        
    return ans

n1 = factorial(N)
n2 = factorial(M)
ans = []
common = []
for p in n1:
    for q in n2:
        if p[0] != q[0]: continue
        common.append(p[0])

        if p[1] > q[1]:
            a = math.ceil(p[1] / 2)
            ans.append((p[0], a))
        else:
            a = math.ceil(q[1] / 3)
            ans.append((q[0], a)) 

for p in n1:
    if not p[0] in common: 
        a = math.ceil(p[1] / 2)
        ans.append((p[0], a))
        
for p in n2:
    if not p[0] in common:
        a = math.ceil(p[1] / 3) 
        ans.append((p[0], a))

res = 1
for i, c in ans:
    res *= i**c

print(ans)
print(res)
            