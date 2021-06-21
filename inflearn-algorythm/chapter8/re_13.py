# 플로이드 워셜 알고리즘

import sys

n,m = map(int, sys.stdin.readline().split())
connect = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    st, en, cost = map(int, sys.stdin.readline().split())
    connect[st][en] = cost


for i in range(n+1):
    connect[i][i] = 0

# for x in connect:
#     print(x)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if connect[i][j] > connect[i][k] + connect[k][j]:
                connect[i][j] = connect[i][k] + connect[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if connect[i][j] == float('inf'):
            print("M", end=" ")
        else :
            print(connect[i][j], end=" ")
    print()

