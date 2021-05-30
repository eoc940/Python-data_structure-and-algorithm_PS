# 합이 같은 부분집합

import sys

def dfs(v) :
    global flag
    if v==n :
        tmp = []
        for i in range(len(ch)) :
            if ch[i] != 0 :
                tmp.append(ch[i])
        if tmp :
            group.append(tmp)
        #print(tmp, sum(tmp) ,sum(num))
        if sum(tmp)*2 == sum(num) :
            #print("????")
            flag = True
            return

    else :
        ch[v] = num[v]
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)


n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
ch = [0]*n
group = []
flag = False
dfs(0)

if flag :
    print("YES")
else :
    print("NO")






