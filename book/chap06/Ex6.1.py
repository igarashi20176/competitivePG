import bisect
res = []
a = [10, 5, 2, 27, 1, 17, 17]

b = sorted(a)
print(b)


for i in range(len(a)):
    res.append(bisect.bisect_left(b, a[i]))

print(res)


    


