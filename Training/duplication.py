A, B, C, D = [ int(i) for i in input().split() ]

upper = max(A, C)
lower = min(B, D)

print(lower - upper) if lower - upper > 0 else print(0)
