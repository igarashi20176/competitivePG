def judge(bit):
    cnt = [0] * m  # 電球mに対応するボタンが何回押されたか
    for i in range(n):
        if not ((bit >> i) & 1):
            continue

        for x in s[i]:
            cnt[x] += 1

    for c, p in zip(cnt, P):
        # 全ての電球が点灯しない場合
        if c % 2 != p:
            return False
    
    # 全ての電球が点灯する場合
    return True    
    

n, m = map(int, input().split())

# s[i]...ボタンiに対応
s = [[] for _ in range(n)]
for i in range(m):
    k, *S = map(int, input().split())

    # ボタンに対応する電球mを配列に格納
    for j in S:
        s[j-1].append(i)    

P = list(map(int, input().split()))
        
    
ans = 0
for i in range(2**n):
    ans += judge(i)

print(ans)