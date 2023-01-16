# 目標金額
M = 1800
coins = [500, 100, 50, 10, 5, 1]
# 枚数
a = [3, 2, 1, 9, 6, 10]

res = 0
for i in range(6):
    add = M // coins[i]

    # 枚数制限以上だった場合，枚数制限に抑える
    if add > a[i]:
        add = a[i]
    
    M -= coins[i] * add
    res += add

print(res)