SS = input()
SSl = len(SS)
T = input()
Tl = len(T)


ans = []
for i in range(SSl, Tl-1, -1):
    L = i - Tl

    ok = True
    for i in range(len(T)):
        if SS[L+i] != "?" and SS[L+i] != T[i]: 
            ok = False
            break

    if ok: 
        for i in range(L):
            if SS[i] == "?":
                ans.append("a")
            else:
                ans.append(SS[i])
        
        ans.append(T)


print("".join(ans)) if len(ans) else print("UNRESTORABLE")


    

