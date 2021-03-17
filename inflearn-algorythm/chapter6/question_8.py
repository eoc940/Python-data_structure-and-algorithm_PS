# 순열 구하기

def DFS(L) :
    global cnt

    if L==m:
        for i in range(m) :
            print(res[i], end=" ")
        cnt += 1
        print()
    else:
        for i in range(1,n+1) :
            # 레벨별 값이 같을때를 제외하는 로직
            if ch[i]==0 :
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0


n, m = map(int, input().split())
cnt = 0
ch = [0]*(n+1)
res = [0]*n
DFS(0)
print(cnt)


