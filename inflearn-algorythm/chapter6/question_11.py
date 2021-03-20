# 수들의 조합

def DFS(L, s, tot) :
    global cnt
    if L==k and tot%m==0:
        cnt += 1
    else:
        for i in range(s, n) :
            res[L] = a[i]
            DFS(L+1, i+1, tot+res[L])

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
res = [0]*(n+1)
DFS(0,0,0)
print(cnt)
