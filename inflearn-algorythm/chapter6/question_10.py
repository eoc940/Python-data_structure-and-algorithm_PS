# 조합 구하기

def DFS(v, s) :
    if v==m :
        global cnt
        for i in range(m) :
            print(res[i], end=" ")
        print()
        cnt += 1
    else:
        for i in range(s,n+1) :
            res[v] = i
            DFS(v+1, i+1)

n, m = map(int, input().split())
cnt = 0
ch = [0]*(n+1)
res = [0]*n
DFS(0, 1)
print(cnt)