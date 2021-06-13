# 피자 배달 거리(DFS활용)

import sys
import heapq

n,m = map(int, sys.stdin.readline().split())
_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pizza = []
home = []

for i in range(n):
    for j in range(n):
        if _map[i][j]==2:
            pizza.append((i,j))
        if _map[i][j]==1:
            home.append((i,j))
# print(pizza)

def dfs(v,s) :
    if v==m :
        tmp = []
        for i in range(m) :
            tmp.append(ch[i])
        group.append(tmp)
    else :
        for i in range(s,len(pizza)):
            ch[v] = pizza[i]
            dfs(v+1, i+1)


ch = [0]*len(pizza)
group = []
dfs(0,0)

answer = float('inf')

for x in group :
    total = 0
    for house in home :
        tmp = []
        heapq.heapify(tmp)
        for piz in x :
            dist = abs(house[0]-piz[0])+abs(house[1]-piz[1])
            heapq.heappush(tmp,dist)
        total += heapq.heappop(tmp)
    if answer > total :
        answer = total

print(answer)








