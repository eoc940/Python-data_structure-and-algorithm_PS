# DFS와 BFS
# 백준에서는 입력받을때 input보다는 sys.stdin.readline()을 쓰자
# 이게 더 빠르다
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
connect = [[0] * (n+1) for i in range(n+1)]
check = [0] * (n+1)

for _ in range(m):
    start, finish = map(int, sys.stdin.readline().split())
    connect[start][finish] = 1
    connect[finish][start] = 1

def DFS(vertex) :
    if check[vertex]==1 :
        return
    print(vertex, end=" ")
    check[vertex] = 1
    for i in range(1,n+1) :
        if connect[vertex][i]==1 :
            DFS(i)

def BFS(vertex) :
    Q = deque()
    Q.append(vertex)
    check[vertex] = 1
    while Q :
        tmp = Q.popleft()
        print(tmp, end=" ")
        for i in range(1, n+1) :
            if connect[tmp][i]==1 and check[i]==0:
                Q.append(i)
                check[i] = 1

DFS(v)
print()
check = [0] * (n+1) #check초기화
BFS(v)