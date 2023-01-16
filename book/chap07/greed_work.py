from operator import itemgetter


N = 6
work = [(9, 16), (10, 12), (11, 15), (13, 19), (15, 18), (19, 23)]

# タプルの指定したキーでソート
work.sort(key=itemgetter(1))
print(work)


res = 0
current_end_time = 0
for i in range(N):

    # 区間の開始時間が終了時間以下の場合スキップ(区間被り)
    if work[i][0] < current_end_time:
        continue

    current_end_time = work[i][1]
    res+=1

print(res)

    
    