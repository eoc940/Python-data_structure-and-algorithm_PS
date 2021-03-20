# 최대점수 구하기(DFS)
import sys

def DFS(L, ssum, tsum) :
    global maximum
    if tsum > m :
        return

    if L == n:
        if ssum > maximum :
            maximum = ssum
    else :
        DFS(L+1, ssum+a[L][0], tsum+a[L][1])
        DFS(L+1, ssum, tsum)

n, m = map(int, input().split())
a = []
ch = [0]*(n+1)
maximum = 0
for i in range(n) :
    score, time = map(int, input().split())
    a.append((score, time))

DFS(0,0,0)
print(maximum)