N = int(input())

def yakusu(n):
    ans = []
    i = 1
    while i * i <= n:
        if not n % i:
            ans.append(i)

            if n // i != i:
                ans.append(n // i)
        i+=1
    
    return ans

print(sorted(yakusu(N)))
