# 동전교환

import sys

def DFS(v, sum) :
    global res
    # 최소의 v를 찾으므로 v가 res를 넘어가는 순간 return
    print(v,sum,res)
    if v >= res :
        return
    if sum > tot :
        return
    if sum == tot :
        if v < res :
            res = v
    else:
        for i in range(n) :
            DFS(v+1, sum+a[i])

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
tot = int(input())
res = 2147000000
DFS(0, 0)
print(res)


