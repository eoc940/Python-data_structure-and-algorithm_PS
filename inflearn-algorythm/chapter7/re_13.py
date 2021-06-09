# 섬나라 아일랜드(BFS활용)

import sys
from collections import deque

n = int(sys.stdin.readline())
island = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(x,y) :
    dq = deque()
    island[x][y] = 0
    dq.append((x,y))
    while dq :
        tmp = dq.popleft()
        for i in range(8) :
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0<=xx<n and 0<=yy<n and island[xx][yy] == 1 :
                island[xx][yy] = 0
                dq.append((xx,yy))

def dfs(x,y) :
    island[x][y] = 0
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and island[xx][yy] == 1:
            dfs(xx,yy)

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]
cnt = 0

for i in range(n) :
    for j in range(n):
        if island[i][j]==1 :
            #print(i,j)
            #bfs(i,j)
            dfs(i,j)
            cnt += 1

print(cnt)


