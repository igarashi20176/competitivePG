N = 5
h = [1, 1, 1, 1, 1]
s = [1, 2, 1, 2, 1]

left, right = 0, 100

while right - left > 1:
    mid = (left + right) // 2

    ok = True
    t = []

    for i in range(N):
        if mid < h[i]:
            ok = False
        else:
            t.append((mid - h[i]) / s[i])
            
    t.sort()
    
    for i in range(N):
        if t[i] < i:
            print(t[i],  i)
            ok = False
    
    if ok:
        right = mid
    else:
        left = mid
    
print(right)
            
            
    