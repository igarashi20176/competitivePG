A, B, C = [ int(i) for i in input().split() ]

ans = False
for i in range(B):
    if A * i % B == C:
        ans = True
        break

print("YES") if ans else print("NO")