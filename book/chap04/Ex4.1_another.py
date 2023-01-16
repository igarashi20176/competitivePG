import time

start = time.time()

def tri( n ):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if( n == 2 ):
        return 1
    return tri(n-1) + tri(n-2) + tri(n-3)


print(f'time: {time.time() - start},  res: {tri(10)}')