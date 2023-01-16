num = input()


for i in range(2**(len(num)-1)):
    ans = int(num[0])
    tmp = num[0]
    for j in range(len(num)-1):
        if (i >> j) & 1:
            ans+=int(num[j+1])
            tmp += "+" + num[j+1]
        else:
            ans-=int(num[j+1])
            tmp += "-" + num[j+1]

    if ans == 7:
        print(tmp + "=7")
        break