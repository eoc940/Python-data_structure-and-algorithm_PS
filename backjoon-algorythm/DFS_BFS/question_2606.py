# 바이러스

import sys

n = int(input())
m = int(input())
connect = [[0]*(n+1) for i in range(n+1)]
check = [0] * (n+1)
cnt = 0

for i in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    connect[start][end] = 1
    connect[end][start] = 1

def DFS(vertex) :
    global cnt
    for i in range(1, n+1) :
        if connect[vertex][i]==1 and check[i]==0:
            check[i] = 1
            cnt += 1
            DFS(i)

check[1] = 1
DFS(1)
print(cnt)