from operator import itemgetter

M = int(input("何本買う?: "))

a = [int(i) for i in input("単価: ").split()] 
b = [int(i) for i in input("本数: ").split()] 
c = []

for i in range(len(a)):
    c.append( (a[i], b[i]) )

c.sort(key=itemgetter(0))

res = 0
for i in range(len(c)):
    min_num = min(c[i][1], M)
    res += c[i][0] * min_num
    M -= min_num

print(res)



