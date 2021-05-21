# 봉우리

import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
bong = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n) :
    for j in range(n) :
        if ch[i][j] == 0 :
            flag = True
            for k in range(4) :
                x = i + dx[k]
                y = j + dy[k]
                if 0<=x<n and 0<=y<n :
                    if board[i][j] <= board[x][y] :
                        flag = False
                        break
                    else :
                        ch[x][y] = 1
            if flag :
                bong += 1
print(bong)




