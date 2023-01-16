N = int(input())
a = list(map(int, input().split()))


def even_cnt(array, cnt = 0):
    flg = True
    for i in range(N):
        if array[i] % 2:
            flg = False
    if flg:
        return even_cnt(list(map(lambda x: x/2, array)), cnt+1)

    return cnt

print(even_cnt(a))
