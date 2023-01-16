import bisect

sum = 0
# a = [3, 2, 10, 12, 5, 22]
# b = [3, 7, 3, 8, 10, 11]
# c = [15, 4, 11, 8, 8, 3]
a = [1, 1, 1]
b = [2, 2, 2]
c = [3, 3, 3]


a.sort()
b.sort()
c.sort()

for j in range(len(b)):
    Aj = bisect.bisect_left(a, b[j])
    Cj = len(b) - bisect.bisect_right(c, b[j])
    sum += Aj * Cj

print(sum)