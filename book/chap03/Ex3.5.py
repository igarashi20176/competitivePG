K = 20
N = 42
cnt1 = 0

for x in range(K):
    for y in range(K):
        z = N - x - y
        if z >= 0 and z <= K:
            cnt1+=1

print(cnt1)


