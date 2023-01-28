N = int(input())
S = list(input())

dl = False
for i in range(N):
    if S[i] == '"':
        if dl:
            dl = False
            continue
        dl = True
        continue
    
    if not dl:
        if S[i] == ",":
            S[i] = "."

print("".join(S))

