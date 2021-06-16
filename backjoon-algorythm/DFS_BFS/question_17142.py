# 연구소

import sys
from collections import deque
from itertools import combinations
import copy

def BFS(combin, left):
    global time
    dq = deque(combin)
    time_cnt = 0
    checked = [[0]*n for _ in range(n)]
    for x, y in combin:
        checked[x][y] = 1

    while dq:
        if not left: break #처음부터 left가 0일수 있기 때문에 바로 break
        time_cnt += 1
        if time_cnt >= time : return float('inf')
        for _ in range(len(dq)):
            x,y = dq.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0<=xx<n and 0<=yy<n and location[xx][yy] != 1 and not checked[xx][yy]:
                    checked[xx][yy] = 1
                    dq.append((xx,yy))
                    if location[xx][yy] == 0 :
                        left -= 1
    if not left:
        return time_cnt
    else:
        return float('inf')



n, m = map(int, sys.stdin.readline().split())
location = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

time = float('inf')
virus = []
not_infected = 0

for i in range(n):
    for j in range(n):
        if location[i][j]==2:
            virus.append((i,j))
        if location[i][j]==0:
            not_infected += 1

combin = combinations(virus, m)

for c in combin:
    time = min(time, BFS(c, not_infected))

if time==float('inf'):
    time = -1

print(time)


