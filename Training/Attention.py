N = int(input())
S = input()

E = [0] * N
W = [0] * N

for i in range(N):
    if S[i] == "W":
        W[i] = 1
    else:
        E[i] = 1

# 累積和
for i in range(1, N):
    W[i] += W[i-1]
    E[i] += E[i-1]


ans = 10**6
# i...誰をリーダにするか
for i in range(N):
    sm = 0
    if i:
        sm += W[i-1]
    sm += E[N-1] - E[i]

    ans = min(ans, sm)

print(ans)
    


