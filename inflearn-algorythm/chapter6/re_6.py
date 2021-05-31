# 중복순열 구하기
import sys

n,m = map(int, sys.stdin.readline().split())

def dfs(v) :
    global group
    if v==m :
        tmp = []
        for i in ch :
            if i != 0 :
                tmp.append(i)
        group.append(tmp)
    else :
        for i in range(n) :
            ch[v] = i+1
            dfs(v+1)
            #ch[v] = 0

group = []
ch = [0]*n
dfs(0)
for x in group :
    for i in x :
        print(i, end=" ")
    print()

print(len(group))



