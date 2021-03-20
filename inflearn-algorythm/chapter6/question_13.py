# 경로 탐색(그래프 DFS)
'''
import sys

def DFS(L) :
    global cnt
    if L==n:
        cnt += 1
        for x in res:
            print(x, end=" ")
        print()
    else :
        for i in range(1,n+1) :
            if ch[i] == 0 and a[L][i] == 1 :
                ch[i] = 1
                res.append(i)
                DFS(i)
                res.pop()
                ch[i] = 0

n, m = map(int, input().split())
a = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
res = []
res.append(1)
cnt = 0
for i in range(m) :
    b, c = map(int, input().split())
    a[b][c]=1
ch[1] = 1
DFS(1)
print(cnt)

'''
# 다시 풀어보기

def DFS(L) :
    global cnt
    if L==n:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else :
        for i in range(1, n+1) :
            if ch[i] == 0 and g[L][i] == 1:
                ch[i] = 1
                res.append(i)
                DFS(i)
                res.pop()
                ch[i] = 0

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
cnt = 0
ch = [0]*(n+1)
res = []
res.append(1)
for i in range(m) :
    a, b = map(int, input().split())
    g[a][b] = 1
ch[1] = 1
DFS(1)
print(cnt)

















