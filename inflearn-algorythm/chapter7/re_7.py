# 송아지 찾기(bfs : 상태트리검색)

import sys
from collections import deque

s, e = map(int, sys.stdin.readline().split())

ch = [0]*10001
dq = deque()

dq.append((s,0))
ch[s] = 1
cnt = 0
go = [5,1,-1]

# ch로 방문한 곳이 정답이 아닐때 dq로 넣어주지 않는다

while dq :
    #print(dq)
    tmp = dq.popleft()
    if tmp[0] == e:
        print(tmp[1])
        break
    for x in go :
        if 10000 >= tmp[0]+x >= 0 and ch[tmp[0]+x] == 0 :
            ch[tmp[0]+x] = 1
            dq.append((tmp[0]+x, tmp[1]+1))







