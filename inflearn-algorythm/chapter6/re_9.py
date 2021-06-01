# 수열 추측하기

import sys
n, f = map(int, sys.stdin.readline().split())

def dfs(v) :
    if v==n :
        tmp = []
        for x in ch :
            if x != 0 :
                tmp.append(x)
        group.append(tmp)
    else :
        for i in range(n) :
            if i+1 not in ch :
                ch[v] = i+1
                dfs(v+1)
                ch[v] = 0

ch = [0]*n
group = []
dfs(0)

def weight(num) :
    tmp = [1,1]
    while len(tmp) < num :
        for i in range(len(tmp)-1) :
            tmp[i] = tmp[i] + tmp[i+1]
        tmp.insert(0,1)
        tmp[-1] = 1
    return tmp



for x in group :
    #1번방법
    # copy = x.copy()
    # for i in range(len(copy)-1) :
    #     for j in range(len(copy)-1-i) :
    #         copy[j] = copy[j] + copy[j+1]
    # if copy[0] == f :
    #     for j in x :
    #         print(j, end=" ")
    #     break

    # 2번방법
    wei = weight(len(x))
    total = 0
    for i in range(len(x)) :
        total += x[i]*wei[i]
    if total == f:
        for j in x:

            print(j, end=" ")
        break






