# 특정 거리의 도시 찾기

# 2차원 배열 way를 1차원으로 바꿔야함

from collections import deque
import sys

# 입력받기
N,M,K,X = map(int, sys.stdin.readline().split())

# 노드와 연결노드를 나타내는 dict형 way, 노드를 지났는지 여부와 거리를 알려주는 ch
way = dict()
ch = [-1]*(N+1)

# 입력값을 way에 넣어줌
for x in range(M) :
    stt, end = map(int, sys.stdin.readline().split())
    way[stt] = way.get(stt, []) + [end]

# bfs를 위한 deque 생성, 초기 노드 X를 넣어주고 체크함
dq = deque()
dq.append(X)
ch[X] = 0

# bfs를 통해 X 노드부터의 거리를 ch에 담아줌
while dq :
    tmp = dq.popleft()
    if tmp in way.keys() :
        nodes = way[tmp]
        for node in nodes :
            if ch[node]==-1 :
                dq.append(node)
                ch[node] = ch[tmp]+1

# 조건에 맞게 출력
if K not in ch :
    print(-1)
else :
    for i in range(len(ch)) :
        if ch[i]==K :
            print(i)



