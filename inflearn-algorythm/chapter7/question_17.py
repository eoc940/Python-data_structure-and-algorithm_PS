# 피자 배달 거리

import sys

n, m = map(int, sys.stdin.readline().split())
route = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
stores = []
for x in range(n) :
    for y in range(n) :
        if route[x][y]==2:
            stores.append((x,y))

combin = []
tmp = [(0,0)]*n

def DFS(v, s) :
    if v==m:
        part = []
        for i in range(m) :
            part.append(tmp[i])
        combin.append(part)
        return
    else:
        for i in range(s, len(stores)) :
            tmp[v] = stores[i]
            DFS(v+1, i+1)

DFS(0,0)

# combin이 나온 상태
from collections import deque

def BFS(x, y, li) :
    dq = deque()
    dq.append((x,y))
    global total
    while dq :
        tmp = dq.popleft()
        if tmp in li :
            total += (abs(x-tmp[0])+abs(y-tmp[1]))
            break

        for i in range(4) :
            xx = dx[i] + tmp[0]
            yy = dy[i] + tmp[1]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 :
                ch[xx][yy] = 1
                dq.append((xx,yy))

res = float('inf')
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for li in combin :
    tmp_combin=li
    total = 0
    for i in range(n) :
        for j in range(n) :
            if route[i][j]==1 :
                ch = [[0] * n for _ in range(n)]
                ch[i][j] = 1
                BFS(i,j,li)
    if res > total :
        res = total
print(res)

# 강사님 풀이

import sys
def DFS(L,s) :
    global res
    if L==m :
        sum = 0
        for j in range(len(hs)) :
            x1 = hs[j][0] # 집의 좌표
            y1 = hs[j][1]
            dis = float('inf')
            for x in cb:
                x2 = pz[x][0] # 피자집의 좌표
                y2 = pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum<res:
            res=sum
    else:
        for i in range(s,len(pz)) :
            cb[L] = i
            DFS(L+1, i+1)

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
hs = []
pz = []
cb = [0]*m
res = float('inf')
for i in range(n) :
    for j in range(n) :
        if board[i][j]==1:
            hs.append((i,j))
        elif board[i][j]==2:
            pz.append((i,j))

DFS(0,0)
print(res)

