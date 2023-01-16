li = list(map(int, input().split()))
long = len(li)
ans = 0

odd = []
for i in range(long):
    if li[i] % 2:
       odd.append(i) 

if len(odd) == 1:
    for i in range(long):
        if i in odd: continue
        li[i] += 1
    ans += 1

if len(odd) == 2:
    for i in odd:
        li[i] += 1
    ans += 1


m = max(li)
while True:
    ok = True
    for i in range(long):
        if li[i] < m:
            li[i] += 2
            ans += 1
            ok = False

    if ok: break

print(ans)

    
        
