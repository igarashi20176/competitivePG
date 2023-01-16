N = int(input())
btns = [0]

for i in range(N):
    btns.append(int(input()))



def roop(): 
    cur = 1
    for i in range(1, 10**5):
        cur = btns[cur]

        if cur == 2:
            return i
    
    return -1

print(roop())
    
