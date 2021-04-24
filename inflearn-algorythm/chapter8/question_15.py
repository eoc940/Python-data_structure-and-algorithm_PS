# 위상정렬(그래프 정렬)

import sys
from collections import deque
'''
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m) :
    beg, end = map(int, sys.stdin.readline().rstrip().split())
    graph[beg][end] = 1
    degree[end] += 1

dq = deque()

while True :
    for i in range(1,n+1) :
        if degree[i] == 0 :
            dq.append(i)
            degree[i] = -1
    while dq :
        tmp = dq.popleft()
        print(tmp, end=" ")
        for i in range(1, n+1) :
            if graph[tmp][i]==1 :
                degree[i] -= 1

    if sum(degree) == -1 * n :
        break
'''
# 강사님 풀이

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
dq = deque()
for _ in range(m) :
    beg, end = map(int, sys.stdin.readline().rstrip().split())
    graph[beg][end] = 1
    degree[end] += 1

for i in range(1,n+1) :
    if degree[i] == 0 :
        dq.append(i)

while dq :
    x = dq.popleft()
    print(x, end=" ")
    for i in range(1,n+1) :
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)





