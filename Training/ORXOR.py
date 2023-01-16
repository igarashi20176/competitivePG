from itertools import product

N = int(input())
A = list(map(int, input().split()))

ans = 2**30
for bit in range(2**(N-1)):
    b_or = A[0]
    b_xor = 0
    for i in range(1, N):
        if bit & (1 << (i-1)):
            b_xor ^= b_or
            b_or = 0    
        b_or |= A[i]
    b_xor ^= b_or

    ans = min(ans, b_xor)

print(ans)
    

            