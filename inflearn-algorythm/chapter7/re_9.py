# 미로의 최단거리 통로(BFS활용)

import sys
from collections import deque

_map = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]

L = 0
dq = deque()
dq.append((0,0))
_map[0][0] = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
flag = True

while dq :
    tmp = dq.popleft()

    if tmp == (6,6) :
        print(_map[tmp[0]][tmp[1]])
        flag = False
        break

    for i in range(4) :
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<7 and 0<=y<7 and _map[x][y]==0 :
            _map[x][y] = _map[tmp[0]][tmp[1]] + 1
            dq.append((x,y))

if flag :
    print(-1)
#
# if _map[6][6]==0 :
#     print(-1)








