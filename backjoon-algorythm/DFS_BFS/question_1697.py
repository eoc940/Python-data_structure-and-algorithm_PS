# 숨바꼭질

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
ch = [0]*200001
def bfs(sub, bro):
    dq = deque()
    ch[sub] = 1
    dq.append(sub)
    sec = 0
    while dq:
        for i in range(len(dq)):
            tmp = dq.popleft()
            #print(tmp)
            if tmp-1 >=0 and ch[tmp-1] == 0 :
                ch[tmp-1] = 1
                dq.append(tmp-1)
            if tmp+1<=200000 and ch[tmp+1] == 0 :
                ch[tmp+1] = 1
                dq.append(tmp+1)
            if tmp*2<=200000 and ch[tmp*2] == 0 :
                ch[tmp*2] = 1
                dq.append(tmp*2)
        sec += 1
        #print(dq)
        if k in dq:
            break
    return sec

if n < k:
    print(bfs(n,k))
else :
    print(n-k)

