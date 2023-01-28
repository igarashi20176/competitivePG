N = int(input())
S = input()

ans = [0] * (N-1)
for n in range(N):
    i = n + 1
    for j in range(N):
        if j + i >= N: break
        
        right = j + i
        if S[j] == S[right]: break
        
        ans[n] += 1

for i in range(N-1):
    print(ans[i])
    

    