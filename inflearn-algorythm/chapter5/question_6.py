# 응급실

from collections import deque

n, m = map(int, input().split())
danger_list = list(map(int, input().split()))

idx = m
cnt = 0
while True :
    if danger_list[0]==max(danger_list) :
        if idx == 0 :
            cnt += 1
            print(cnt)
            break
        else:
            cnt += 1
            danger_list.pop(0)
            idx -= 1
    else:
        if idx == 0 :
            danger_list.append(danger_list.pop(0))
            idx = len(danger_list)-1
        else:
            danger_list.append(danger_list.pop(0))
            idx -= 1


# 강사님 풀이

n, m = map(int, input().split())
Q = [(pos,val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True :
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q) :
        Q.append(cur)
    else:
        cnt += 1
        if cur[0]==m:
            print(cnt)
            break




