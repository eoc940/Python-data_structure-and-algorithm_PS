# 양팔저울(dfs)

import sys

k = int(sys.stdin.readline())
chu = list(map(int, sys.stdin.readline().split()))

def dfs(v, wei) :
    if v==k :
        poss.add(abs(wei))
    else :
        dfs(v+1, wei)
        dfs(v+1, wei + chu[v])
        dfs(v+1, wei - chu[v])

poss = set()
dfs(0, 0)
poss.remove(0)
print(sum(chu)-len(poss))



