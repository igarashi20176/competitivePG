# import bisect

N = int(input(">> "))

a = [ int(input(f'数{i+1}: ')) for i in range(N) ]

b = sorted(a)

index = b.index(int(input("要素: ")))

print(index + 1)