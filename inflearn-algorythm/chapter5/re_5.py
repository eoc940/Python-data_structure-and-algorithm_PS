# 공주 구하기(큐)

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
prince = [x+1 for x in range(n)]
prince = deque(prince)
delete = 0

while len(prince) > 1 :
    #print(prince)
    delete += 1
    if delete == k :
        prince.popleft()
        delete = 0
    else :
        tmp = prince.popleft()
        prince.append(tmp)

print(prince[0])




