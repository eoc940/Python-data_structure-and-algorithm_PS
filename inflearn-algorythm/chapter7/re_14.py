# 안전영역(BFS)

import sys
from collections import deque

n = int(sys.stdin.readline())
hei = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


_min = float('inf')
_max = float('-inf')
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for x in hei :
    if min(x) < _min :
        _min = min(x)
    if max(x) > _max :
        _max = max(x)

def bfs(x,y) :
    dq = deque()
    ch[x][y] = 1
    dq.append((x, y))
    while dq:
        for _ in range(len(dq)):
            tmp = dq.popleft()
            for j in range(4):
                xx = tmp[0] + dx[j]
                yy = tmp[1] + dy[j]

                if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and hei[xx][yy] >= i:
                    ch[xx][yy] = 1
                    dq.append((xx, yy))
answer = 0

for i in range(_min, _max) :

    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for a in range(n) :
        for b in range(n) :
            if hei[a][b] >= i and ch[a][b] == 0:
                cnt += 1
                bfs(a,b)

    if cnt > answer :
        answer = cnt


print(answer)

