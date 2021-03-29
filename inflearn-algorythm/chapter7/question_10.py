# 미로탐색(DFS)

def DFS(x, y) :
    global cnt
    if x==6 and y==6 :
        cnt += 1

        return
    else :
        for i in range(4) :
            tx = x + dx[i]
            ty = y + dy[i]
            if 0<=tx<=6 and 0<=ty<=6 and a[tx][ty]==0 and ch[tx][ty]==0:
                ch[tx][ty] = 1
                res.append((tx,ty))
                DFS(tx, ty)
                ch[tx][ty] = 0
                res.pop()

a = [list(map(int, input().split())) for _ in range(7)]
ch = [[0]*7 for _ in range(7)]
res = []
res.append((0,0))
ch[0][0] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
DFS(0,0)
print(cnt)

# 강사님 풀이
'''
def DFS(x, y) :
    global cnt
    if x==6 and y==6 :
        cnt += 1
    else :
        for i in range(4) :
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<=6 and 0 <=yy<= 6 and board[xx][yy]==0 :
                board[xx][yy] = 1
                DFS(xx,yy)
                board[xx][yy] = 0


board = [list(map(int, input().split())) for _ in range(7)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board[0][0] = 1
cnt = 0
DFS(0,0)
print(cnt)
'''
