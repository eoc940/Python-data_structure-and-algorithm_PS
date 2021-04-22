# 플로이드 워샬 알고리즘
'''
import sys

n, m = map(int, sys.stdin.readline().split())
dis = [[5000]*(n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    dis[i][i] = 0
for i in range(m) :
    a,b,c = map(int, sys.stdin.readline().split())
    dis[a][b] = c
# 3중 for문이 플로이드 와샬 알고리즘
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if dis[i][j]==5000:
            print("M", end=" ")
        else:
            print(dis[i][j], end=" ")
    print()

'''





# 다시 풀어보기

import sys

n,m = map(int, sys.stdin.readline().split())
way = [[2000]*(n+1) for _ in range(n+1)]

for _ in range(m) :
    row, col, val = map(int, sys.stdin.readline().split())
    way[row][col] = val

for i in range(1,n+1) :
    way[i][i] = 0
# k 정점을 지나서 i->j로 간다
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            way[i][j] = min(way[i][j], way[i][k] + way[k][j])

# 출력
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if way[i][j]==2000:
            print("M" , end=" ")
        else :
            print(way[i][j], end=" ")
    print()
























