X = input()
S = X[::-1]

a = ["dream", "dreamer", "erase", "eraser"]
for idx, s in enumerate(a):
    a[idx] = s[::-1]
    
can = True
i = 0
while i < len(S):
    can2 = False
    for case in a:
        if S[i:i+len(case)] == case:
            can2 = True
            i += len(case)

    if not(can2):
        can = False
        break

print("YES") if can else print("NO")
    
    
            
        
        
        