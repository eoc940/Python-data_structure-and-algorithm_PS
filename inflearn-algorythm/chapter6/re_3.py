# 부분집합 구하기(DFS)

import sys

def dfs(v) :
    if v==n+1 :
        tmp = []
        for i in range(len(ch)) :
            if ch[i]==1 :
                tmp.append(i)
        if len(tmp) >= 1 :
            groups.append(tmp)
    else :
        ch[v] = 1
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)


n = int(sys.stdin.readline())
groups = []
ch = [0]*(n+1)
dfs(1)
print(groups)



