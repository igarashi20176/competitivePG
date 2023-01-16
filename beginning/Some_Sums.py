N, A, B = map(int, input().split())

# for i in range(1, N+1):
#     tmp = 0
#     for j in str(i):
#         tmp += int(j)
    
#     if tmp >= A and tmp <= B:
#         total += i

def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10

    print(f"sum: {sum}")
    return sum

total = 0
for i in range(1, N+1):
    s = findSumOfDigits(i)
    if s >= A and s <= B:
        total += i

print(total)

    