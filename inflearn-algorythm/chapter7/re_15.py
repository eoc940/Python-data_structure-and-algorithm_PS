# 토마토 BFS 활용

import sys
from collections import deque

m,n = map(int, sys.stdin.readline().rstrip().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dq = deque()
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

for i in range(n) :
    for j in range(m):
        #print(i,j)
        if tomato[i][j] == 1 :
            dq.append((i,j))

def check_ripe() :
    total = 0
    for x in tomato :
        total += sum(x)
    return total

def check_all() :
    for i in range(n):
        for j in range(m) :
            #print(i, j)
            if tomato[i][j] == 0 :

                return False
    return True

while dq :
    prior_ch = check_ripe()
    for _ in range(len(dq)):
        tmp = dq.popleft()
        for i in range(4) :
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0<=x<n and 0<=y<m and tomato[x][y] == 0 :
                tomato[x][y] = 1
                dq.append((x,y))
    after_ch = check_ripe()
    if prior_ch == after_ch :
        # for x in tomato :
        #     print(x)
        if check_all() : # 다 익은 경우
            print(cnt)
            break
        else :
            print(-1)
            break
    cnt += 1


