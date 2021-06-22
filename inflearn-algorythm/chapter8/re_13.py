# 플로이드 워셜 알고리즘

import sys
from collections import defaultdict, deque

n,m = map(int, sys.stdin.readline().split())
connect = defaultdict(list)

for _ in range(m):
    st, en, cost = map(int, sys.stdin.readline().split())
    connect[st].append((en, cost))

#print(connect)

def dfs(x, y, total) :
    global answer
    if x==y:
        #print(total, answer, end=" ")
        if answer > total:
            answer = total
    else :
        for x in connect[x]:
            en, cost = x[0], x[1]
            if ch[en] == 0:
                ch[en] = 1
                dfs(en, y, total + cost)
                ch[en] = 0


for i in range(1,n+1):
    for j in range(1,n+1):
        answer = float('inf')
        ch = [0]*(n+1)
        ch[i] = 1
        dfs(i,j,0)

        if answer == float('inf'):
            print("M", end=" ")
        else :
            print(answer, end=" ")
    print()








'''
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

'''