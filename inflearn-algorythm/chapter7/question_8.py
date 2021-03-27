# 사과나무(BFS)
'''
from collections import deque

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
total = 0
dQ = deque()
dQ.append([n//2, n//2])

while dQ :
    now = dQ.popleft()
    if now[0] in [0,n-1] or now[1] in [0, n-1] :
        break
    for next in ([now[0]-1,now[1]],[now[0]+1,now[1]],[now[0],now[1]-1],[now[0],now[1]+1]) :
        if ch[next[0]][next[1]] == 0 :
            dQ.append(next)
            ch[next[0]][next[1]] = 1
            total += a[next[0]][next[1]]

print(total)
'''
# 다른 풀이
from collections import deque
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
total = 0
dQ = deque()
ch[n//2][n//2] = 1
total += a[n//2][n//2]
dQ.append((n//2,n//2))
L = 0
while True :
    if L == n//2 :
        break
    size = len(dQ)
    for i in range(size) :
        tmp = dQ.popleft()
        for j in range(4) :
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] == 0:
                total += a[x][y]
                ch[x][y] = 1
                dQ.append((x,y))
    L += 1

print(total)