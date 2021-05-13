# 특정 거리의 도시 찾기

# 2차원 배열 way를 1차원으로 바꿔야함

from collections import deque
import sys

N,M,K,X = map(int, sys.stdin.readline().split())
way = dict()
ch = [-1]*(N+1)

for x in range(M) :
    stt, end = map(int, sys.stdin.readline().split())
    way[stt] = way.get(stt, []) + [end]

dq = deque()
dq.append(X)
ch[X] = 0

while dq :
    tmp = dq.popleft()
    if tmp in way.keys() :
        nodes = way[tmp]
        for node in nodes :
            if ch[node]==-1 :
                dq.append(node)
                ch[node] = ch[tmp]+1

if K not in ch :
    print(-1)
else :
    for i in range(len(ch)) :
        if ch[i]==K :
            print(i)



