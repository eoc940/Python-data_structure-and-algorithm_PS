# 단지번호 붙이기(DFS, BFS)

# DFS로 풀기

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
