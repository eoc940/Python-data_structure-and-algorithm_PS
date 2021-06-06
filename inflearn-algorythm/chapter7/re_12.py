# 단지 번호 붙이기(dfs,bfs)

import sys

n = int(sys.stdin.readline().rstrip())

home = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]


def dfs(x,y) :
    global cnt
    cnt += 1
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]

        if 0<=xx<n and 0<=yy<n and home[xx][yy] == 1:
            home[xx][yy] = 0
            #print(xx, yy)
            dfs(xx,yy)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
complex = []

for i in range(n) :
    for j in range(n):
        cnt = 0
        if home[i][j] == 1 :
            home[i][j] = 0
            dfs(i,j)
            # dfs를 실행한 후의 cnt를 append해주어야 한다
            complex.append(cnt)

complex.sort()
print(len(complex))
for x in complex :
    print(x)






