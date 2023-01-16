import bisect

def main():
    N, M = map(int, input().split())

    points = [int(input()) for _ in range(N)] + [0]

    sum = set()
    for i in range(len(points)):
        for j in range(len(points)):
            sum.add(points[i] + points[j])


    sum = sorted(list(sum))

    ans = 0
    for a in sum:
        rest = M-a
        if rest < 0: continue

        idx = bisect.bisect_right(sum, rest)
        
        if idx <= 0:
            ans = max(ans, a)
        else:
            tmp = a + sum[idx-1]
            ans = max(ans, tmp)

    print(ans)
    return

    
if __name__ == '__main__':
    main()