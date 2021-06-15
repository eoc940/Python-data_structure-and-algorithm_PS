# 연구소

import sys
from collections import deque
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().split())
location = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

virus = []
not_infected = 0

for i in range(n):
    for j in range(n):
        if location[i][j]==2:
            virus.append((i,j))

combi = combinations(virus, m)
#print(combi)

answer = float('inf')

for x in combi:
    time = [[0] * n for _ in range(n)]
    loca = copy.deepcopy(location)
    dq = deque(x)
    result = 0
    while dq:
        tmp = dq.popleft()
        #print(tmp)
        for i in range(4):
            xx = dx[i] + tmp[0]
            yy = dy[i] + tmp[1]
            if 0<=xx<n and 0<=yy<n and loca[xx][yy]==0 and time[xx][yy]==0 :
                dq.append((xx,yy))
                loca[xx][yy] = 2
                time[xx][yy] = time[tmp[0]][tmp[1]] + 1
        if not dq :
            result = time[tmp[0]][tmp[1]]
    flag = 1
    for j in range(n):
        for k in range(n):
            if loca[j][k] == 0:
                flag = 0

    if flag == 0:
        result = -1
        # for a in range(n):
        #     for b in range(n):
        #         if time[a][b] > result:
        #             result = time[a][b]
    # else :
    #     result = -1

    if result != -1 :
        if answer > result:
            answer = result
    #print(result)


if answer==float('inf') :
    print(-1)
else :
    print(answer)




