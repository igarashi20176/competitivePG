N = int(input())

W = []
for i in range(N):
    w = int(input())
    W.append(w)

v = []
v.append(W[0])

# v[j] - W[i]が最小となる山に重ねていく → vの最小化
for i in range(1, N):
    idx = -1
    for j in range(len(v)):
        if W[i] > v[j]: continue
            
        if idx == -1: 
            idx = j
        else:
            if v[idx] > v[j]:
                idx = j

    if idx == -1:
        v.append(W[i])
    else:
        v[idx] = W[i]

print(len(v))
    