# 동전 분배하기(dfs)

import sys

n = int(sys.stdin.readline())

coin = [int(sys.stdin.readline()) for _ in range(n)]

def dfs(v) :
    global mini
    if v==n :
        ch_set = set(ch)
        if len(ch_set)==len(ch) and max(ch) - min(ch) < mini :
            #print(ch)
            mini = max(ch) - min(ch)

    else :
        for i in range(3) :
            ch[i] += coin[v]
            dfs(v+1)
            ch[i] -= coin[v]

ch = [0]*3
mini = float('inf')
dfs(0)
print(mini)







