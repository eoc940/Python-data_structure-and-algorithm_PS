# 미로탐색(DFS)

import sys

def dfs(x, y) :
    global cnt
    if x==6 and y==6 :
        cnt += 1
        #print()
        return
    else :
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<7 and 0<=yy<7 and way[xx][yy] == 0 :
                way[xx][yy] = 1
                a = (xx, yy)
                #print(a, end=" ")
                dfs(xx,yy)
                way[xx][yy] = 0

way = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
cnt = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
way[0][0] = 1
dfs(0,0)
print(cnt)









