# 안전영역(BFS)

from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
mini = float('inf')
maxi = float('-inf')
for i in range(n) :
    for j in range(n) :
        if mini > a[i][j] :
            mini = a[i][j]
        if maxi < a[i][j] :
            maxi = a[i][j]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
Q =deque()
res = 0

for k in range(mini-1, maxi) : # 최소-1부터 최대-1까지 돈다(최대는 안돌아도 된다)
    cnt = 0
    ch = [[0]*n for _ in range(n)]
    for b in range(n) :
        for c in range(n) :
            if ch[b][c] == 0 and a[b][c] > k:
                Q.append((b,c))
                cnt += 1
                ch[b][c] = 1

                while Q :
                    tmp = Q.popleft()
                    for d in range(4) :
                        x = dx[d] + tmp[0]
                        y = dy[d] + tmp[1]
                        if 0<=x<n and 0<=y<n and a[x][y]>k  and ch[x][y] == 0:
                            Q.append((x,y))
                            ch[x][y] = 1
    if res < cnt :
        res = cnt

print(res)


# 강사님 풀이
'''
def DFS(x,y,h) :
    ch[x][y] = 1
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx,yy,h)

n = int(input())
res = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = [list(map(int,input().split())) for _ in range(n)]
for h in range(100) :
    ch=[[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if ch[i][j]==0 and board[i][j]>h:
                cnt += 1
                DFS(i,j,h)

    res = max(res, cnt)
    if cnt==0:
        break
print(res)
'''

