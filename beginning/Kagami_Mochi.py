N = int(input())
a = []

for i in range(N):
    a.append(int(input()))

b = sorted(a, reverse=True)

cnt = 1
tmp = 0
for i in range(N):
    if i == 0:
        tmp = b[0]

    if tmp > b[i]:
        cnt+=1
        tmp = b[i]


print(cnt) 

