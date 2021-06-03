# 경로탐색(dfs)

import sys

n,m = map(int, sys.stdin.readline().split())
link = [map(int, sys.stdin.readline().split()) for _ in range(m)]
print(link)
way = [[0]*(n+1) for _ in range(n+1)]

for st, en in link :
    way[st][en] = 1

# for x in way :
#     for y in x :
#         print(y, end=" ")
#     print()

def dfs(v) :
    global cnt
    if v==n :
        print(res)
        cnt += 1
        return
    else :
        for i,x in enumerate(way[v]) :
            if x == 1 and ch[i] == 0:
                ch[i] = 1
                res.append(i)
                dfs(i)
                res.pop()
                ch[i] = 0

res = [] # 순서 확인해보기 위한 리스트
res.append(1)
ch = [0]*(n+1)
cnt = 0
ch[1] = 1
dfs(1)
print(cnt)










