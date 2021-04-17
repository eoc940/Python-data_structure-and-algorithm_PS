# 알리바바와 40인의 도둑(bottom-up)

import sys

n = int(sys.stdin.readline())
way = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = way[0][0]

xx = [-1,0]
yy = [0,-1]
for i in range(n) :
    for j in range(n) :
        tmp = []
        for k in range(2) :
            x = xx[k] + i
            y = yy[k] + j
            if 0<=x<n and 0<=y<n :
                tmp.append(dy[x][y])
        if i==0 and j==0 :
            continue
        dy[i][j] = min(tmp) + way[i][j]
print(dy[n-1][n-1])





