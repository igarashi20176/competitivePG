import time

start = time.time()

memo = [-1] * 50

def tri( n ):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if( n == 2 ):
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = tri(n-1) + tri(n-2) + tri(n-3)

    return memo[n]


print(f'time: {time.time() - start},  res: {tri(10)}')