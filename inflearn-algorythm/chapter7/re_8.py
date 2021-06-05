# 사과나무(bfs)

import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dq = deque()
total = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ch = [[0]*n for _ in range(n)]
total += tree[n//2][n//2]
dq.append((n//2,n//2))
ch[n//2][n//2] = 1

L = 0
'''
while dq :
    if L==n//2 :
        break
    else :
        for x in range(len(dq)) :
            tmp = dq.popleft()
            for i in range(4):
                x = tmp[0] + dx[i]  # x, y는 탐색할 좌표
                y = tmp[1] + dy[i]
                if 0 <= x < n and 0 <= y < n:
                    if ch[x][y] == 0:
                        ch[x][y] = 1
                        dq.append((x, y))
                        total += tree[x][y]
                        #print(tree[x][y])
    L += 1
'''

flag = True
while dq and flag:
    tmp = dq.popleft()
    for i in range(4) :
        x = tmp[0] + dx[i] # x, y는 탐색할 좌표
        y = tmp[1] + dy[i]
        if 0<=x<n and 0<=y<n :
            if ch[x][y] == 0 :
                ch[x][y] = 1
                dq.append((x,y))
                total += tree[x][y]
                #print(tree[x][y])
        else :
            flag = False
            break


print(total)
