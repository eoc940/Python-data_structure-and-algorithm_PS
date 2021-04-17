import sys

def DFS(x,y) :
    if dy[x][y] > 0 :
        return dy[x][y]

    if x==0 and y==0 :
        dy[0][0] = way[0][0]
        return dy[0][0]
    else:
        if y==0 :
            dy[x][y]=DFS(x-1,y) + way[x][y]
        elif x==0:
            dy[x][y]=DFS(x,y-1) + way[x][y]
        else:
            dy[x][y]=min(DFS(x - 1, y), DFS(x, y - 1)) + way[x][y]
        return dy[x][y]

n = int(sys.stdin.readline())
way = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = way[0][0]


print(DFS(n-1,n-1))




