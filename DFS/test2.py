A = (1<<2) | (1<<3) | (1<<5) | (1<<7)

bit = A
while bit:
    ans = ""
    for i in range(8):
        if bit & (1<<i):
            ans+=str(i)
    print(ans)
    bit = (bit-1) & A

