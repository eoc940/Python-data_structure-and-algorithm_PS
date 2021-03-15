# 중복순열
'''
def DFS(L) :
    if L == m:
        for j in range(m) :
            print(res[j], end=" ")
        print()
        global cnt
        cnt += 1
    else :
        for i in range(1,n+1) :
            res[L] = i
            DFS(L+1)

n, m = map(int, input().split())
res = [0]*n
cnt = 0
DFS(0)
print(cnt)
'''
# 다시풀기

def DFS(v) :

    if v==m :
        global cnt
        for j in range(m) :
            print(res[j], end=" ")
        cnt += 1
        print()
    else :
        for i in range(1,n+1) :
            res[v] = i
            DFS(v+1)

n, m = map(int, input().split())

cnt = 0
res = [0]*n
DFS(0)
print(cnt)
















