# 미로의 최단거리 통로(BFS활용)
'''
from collections import deque
a = [list(map(int, input().split())) for _ in range(7)]
ch = [[0]*7 for _ in range(7)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

Q = deque()
Q.append((0,0))
L = 0
ch_break = False
while True :
    size = len(Q)
    for i in range(size) :
        now = Q.popleft()
        if now == (6, 6):
            ch_break = True
            break
        for j in range(4) :
            x = now[0] + dx[j]
            y = now[1] + dy[j]
            if x<=6 and y<=6 and x>=0 and y>=0 and a[x][y] == 0 and ch[x][y] == 0:
                Q.append((x,y))
                ch[x][y] = 1
        after_size = len(Q)

    if ch_break :
        break
    if len(Q) == 0 :
        L = -1
        break
    L += 1

print(L)
'''
# 강사님 풀이
from collections import deque
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
Q = deque()
Q.append((0,0))
board[0][0] = 1

while Q :
    tmp = Q.popleft()
    for i in range(4) :
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if dis[6][6]==0:
    print(-1)
else :
    print(dis[6][6])


