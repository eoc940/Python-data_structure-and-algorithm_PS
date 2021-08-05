# 음료수 얼려 먹기

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
ices = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    global answer
    dq = deque()
    dq.append((x,y))
    ices[x][y] = 1
    while dq:
        tx, ty = dq.popleft()
        for i in range(4):
            xx = tx + dx[i]
            yy = ty + dy[i]
            if 0<=xx<n and 0<=yy<m and ices[xx][yy] == 0:
                ices[xx][yy] = 1
                dq.append((xx,yy))
    answer += 1

for i in range(n):
    for j in range(m):
        if ices[i][j] == 0: bfs(i,j)

print(answer)