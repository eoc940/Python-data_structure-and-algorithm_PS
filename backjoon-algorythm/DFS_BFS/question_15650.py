# n과m

import sys

n,m = map(int, sys.stdin.readline().split())

def dfs(v) :
    if v==m :
        tmp = []
        for x in ch :
            if x != 0 :
                tmp.append(x)
        group.append(tmp)
    else :
        for i in range(n) :
            if i+1 > ch[v-1] :
                ch[v] = i+1
                dfs(v+1)

group = []
ch = [0]*n
dfs(0)
for x in group :
    for y in x :
        print(y, end=" ")
    print()

