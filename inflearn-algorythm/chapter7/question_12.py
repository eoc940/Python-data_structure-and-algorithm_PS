# 단지번호 붙이기(DFS, BFS)

# DFS로 풀기
'''
def DFS(x,y) :
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4) :
        xx = dx[i] + x
        yy = dy[i] + y
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx,yy)
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
res = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1:
            cnt = 0
            DFS(i,j)
            res.append(cnt)

res.sort()
print(len(res))
for x in res :
    print(x)

'''




# 다시풀기

def DFS(x,y) :
    global cnt
    a[x][y] = 0
    cnt += 1
    for i in range(4) :
        xx = dx[i] + x
        yy = dy[i] + y
        if 0<=xx<n and 0<=yy<n and a[xx][yy] == 1 :
            DFS(xx,yy)


n = int(input())
a = [list(map(int, input())) for _ in range(n)]
res = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n) :
    for j in range(n) :
        if a[i][j] == 1:
            cnt = 0
            DFS(i,j)
            res.append(cnt)
res.sort()
print(len(res))
for x in res :
    print(x)

# BFS로 풀어보기
from collections import deque
n = int(input())
a = [list(map(int, input())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
res = []
dQ = deque()
for i in range(n) :
    for j in range(n) :
        cnt = 0
        if a[i][j] == 1:
            cnt += 1
            a[i][j] = 0
            dQ.append((i,j))
            while(dQ) :
                tmp = dQ.popleft()
                for k in range(4) :
                    xx = dx[k] + tmp[0]
                    yy = dy[k] + tmp[1]
                    if 0<=xx<n and 0<=yy<n and a[xx][yy] == 1:
                        dQ.append((xx,yy))
                        a[xx][yy] = 0
                        cnt += 1
            res.append(cnt)
res.sort()
print(len(res))
for x in res :
    print(x)




























