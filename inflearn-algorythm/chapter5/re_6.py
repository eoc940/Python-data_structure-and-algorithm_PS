# 응급실

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

danger = list(map(int, sys.stdin.readline().split()))
danger = deque(danger)
mapping = []
cnt = 0

for i, v in enumerate(danger) :
    mapping.append((i,v))
mapping = deque(mapping)
# 계산
while True :

    maxi = 0
    for x in mapping :
        if x[1] > maxi :
            maxi = x[1]
    #print(cnt, mapping)
    tmp = mapping.popleft()
    if maxi==tmp[1] and m==tmp[0] :
        cnt += 1
        break
    elif maxi==tmp[1] and m!=tmp[0] :
        cnt += 1
    else :
        mapping.append(tmp)

print(cnt)




