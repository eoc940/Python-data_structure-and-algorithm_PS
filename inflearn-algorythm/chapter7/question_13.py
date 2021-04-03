# 섬나라 아일랜드(BFS활용)
from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
dQ = deque()
for i in range(n) :
    for j in range(n) :
        if a[i][j] == 1 :
            dQ.append((i,j))
            cnt += 1
            a[i][j] = 0
            while dQ :
                tmp = dQ.popleft()
                for k in range(8) :
                    xx = dx[k] + tmp[0]
                    yy = dy[k] + tmp[1]
                    if 0<=xx<n and 0<=yy<n and a[xx][yy] == 1:
                        dQ.append((xx,yy))
                        a[xx][yy] = 0
print(cnt)






