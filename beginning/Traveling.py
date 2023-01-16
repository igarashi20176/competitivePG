N = int(input())

t = [0]
x = [0]
y = [0]

for i in range(N):
    a = list(map(int, input().split()))
    t.append(a[0])
    x.append(a[1])
    y.append(a[2])

can = True
for i in range(N):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    
    if dt < dist:
        can = False
    
    if dt % 2 != dist % 2:
        can = False

print("Yes") if can else print("No")



