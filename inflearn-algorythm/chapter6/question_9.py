# 수열 추측하기

import sys
'''
def DFS(L, sum) :
    if L==n and sum==f:
        for x in p:
            print(x, end=" ")
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i] = 0


n, f = map(int, input().split())
p = [0]*n
b = [1]*n # 이항계수
ch = [0]*(n+1)
for i in range(1,n) :
    b[i] = b[i-1]*(n-i)//i  # 콤비네이션 구하는 방법

DFS(0,0)
'''

def DFS(L, sum) :
    if L==n and sum==f :
        for i in range(n) :
            print(p[i], end=" ")
        sys.exit(0)
    else:
        for i in range(1, n+1) :
            if ch[i]==0 :
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+p[L]*b[L])
                ch[i] = 0




n, f = map(int, input().split())
p = [0]*n #순열을 만들기 위한 리스트
b = [1]*n #이항계수를 만들기 위한 리스트
ch = [0]*(n+1)
for i in range(1, n) :
    b[i] = b[i-1]*(n-i)//i
DFS(0,0)
