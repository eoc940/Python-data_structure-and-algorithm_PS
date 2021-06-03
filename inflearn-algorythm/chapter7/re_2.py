# 휴가(dfs)

import sys

n = int(sys.stdin.readline())

work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def dfs(v, total) :
    global _max
    if v > n : # 휴가 못감 ㅠㅠ
        return
    if v==n :
        if total > _max :
            _max = total
    else :
        dfs(v+work[v][0], total+work[v][1])
        dfs(v+1, total)

_max = 0
dfs(0,0)
print(_max)










