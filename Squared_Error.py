N = input()
A = list(map(int, input().split()))


cnt = [0] * 400
for i in A:
    cnt[i+200]+=1

ans = 0
for i in range(400):
    for j in range(400):
        if i > j: continue
        ans += cnt[i] * cnt[j] * ((i - j)**2)

print(ans)

    
    



