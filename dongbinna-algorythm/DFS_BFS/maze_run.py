# 미로 탈출

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

dq = deque()
dq.append((0,0))


while dq:
    for _ in range(len(dq)):
        tx, ty = dq.popleft()
        if tx == n-1 and ty == m-1 :
            answer = maze[tx][ty]
            break
        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]
            if 0<=x<n and 0<=y<m and maze[x][y]==1:
                maze[x][y] = maze[tx][ty] + 1
                dq.append((x,y))
    for x in maze:
        print(x)
    print()

print(answer)

