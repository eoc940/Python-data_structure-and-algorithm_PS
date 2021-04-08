# 토마토(BFS)활용

from collections import deque
import sys
m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
day = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
time = 0
dq = deque()
total_if_success = 0
for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1:
            dq.append((i,j))

while dq:
    tmp = dq.popleft()
    for j in range(4) :
        x = dx[j] + tmp[0]
        y = dy[j] + tmp[1]
        if 0<=x<n and 0<=y<m and tomato[x][y]==0 :
            dq.append((x,y))
            tomato[x][y] = 1
            day[x][y] = day[tmp[0]][tmp[1]]+1
flag = 1
for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(n):
        for j in range(m):
            if day[i][j] > result :
                result = day[i][j]
else :
    result = -1

print(result)

