# 바둑이 승차(DFS)

import sys

c, n = map(int, sys.stdin.readline().split())
wei = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

def dfs(v, w) :
    global maxi
    if w + total - sum(wei[:v]) < maxi :
        return
    if w > c :
        return
    if v==n :
        if w > maxi :
            maxi = w
    else :
        dfs(v+1, w+wei[v])
        dfs(v+1, w)

total = sum(wei)
maxi = 0
dfs(0,0)
print(maxi)






