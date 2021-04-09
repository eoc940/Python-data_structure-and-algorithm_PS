# 사다리 타기(DFS)
import sys

def DFS(x, y) :
    if x==0 :
        print(y)

    else:
        if 0<=y-1<=9 and ladder[x][y-1]==1 and check[x][y-1]==0:
            check[x][y-1] = 1
            DFS(x, y-1)
        elif 0<=y+1<=9 and ladder[x][y+1]==1 and check[x][y+1]==0:
            check[x][y+1] = 1
            DFS(x, y+1)
        else :
            check[x-1][y] = 1
            DFS(x-1, y)

ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
check = [[0]*10 for _ in range(10)]
destin = 0

for i in range(10) :
    if ladder[9][i] == 2 :
        destin = i
        break

check[9][destin] = 1
DFS(9,destin)





