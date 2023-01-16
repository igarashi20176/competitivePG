from itertools import product

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0

for row_bit in product(range(2)):
    print(row_bit)