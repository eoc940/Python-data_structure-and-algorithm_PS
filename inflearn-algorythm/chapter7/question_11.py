# 등산경로(DFS)


def DFS(x,y) :
    global cnt
    if x==end[0] and y==end[1] :
        cnt += 1
        return
    else :
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and a[xx][yy] > a[x][y] and ch[xx][yy]==0 :
                ch[xx][yy] = 1
                DFS(xx,yy)
                ch[xx][yy] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
maxi = float('-inf')
mini = float('inf')
start = (0,0)
end = (0,0)
cnt = 0

for j in range(n) :
    for k in range(n) :
        if a[j][k] > maxi :
            maxi = a[j][k]
            end = (j, k)
        if a[j][k] < mini :
            mini = a[j][k]
            start = (j, k)
ch[start[0]][start[1]] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
DFS(start[0],start[1])
print(cnt)






