# 최대점수 구하기(DFS)
import sys
'''
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


'''

# 다시 풀기

def DFS(L, score, time) :
    global res
    if time > m :
        return

    if L==n:
        if score > res :
            res = score
    else :
        DFS(L+1, score + score_li[L], time + time_li[L])
        DFS(L+1, score, time)

n, m = map(int, input().split())
score_li = []
time_li = []
res = 0
for i in range(n) :
    a, b = map(int, input().split())
    score_li.append(a)
    time_li.append(b)

DFS(0,0,0)
print(res)














