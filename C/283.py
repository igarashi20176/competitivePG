from collections import deque

S = deque(list(input()))

ans = 0
while(len(S)):
    ft = S.popleft()
    if not len(S): 
        ans += 1
        continue
    sc = S.popleft()

    if not (ft == "0" and sc == "0"):
        ans += 1

    ans += 1

print(ans)
