# 등산경로(DFS)

import sys

n = int(sys.stdin.readline())
hei = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mini = float('inf')
maxi = float('-inf')
min_idx = (0,0)
max_idx = (0,0)

for i in range(n) :
    for j in range(n):
        if hei[i][j] > maxi :
            max_idx = (i,j)
            maxi = hei[i][j]
        if hei[i][j] < mini :
            min_idx = (i,j)
            mini = hei[i][j]

def dfs(x, y) :
    global cnt
    if x==max_idx[0] and y==max_idx[1] :
        cnt += 1
        return
    else :
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]

            if 0<=xx<n and 0<=yy<n and hei[xx][yy] > hei[x][y] and ch[xx][yy] == 0:
                #print(xx, yy)
                ch[xx][yy] = 1
                dfs(xx, yy)
                ch[xx][yy] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

ch = [[0]*n for _ in range(n)]

ch[min_idx[0]][min_idx[1]] = 1
dfs(min_idx[0], min_idx[1])
print(cnt)







