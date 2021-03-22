# 동전 바꿔주기(DFS)

def DFS(v, ssum) :
    global cnt
    if ssum > T :
        return
    if v==k :
        if ssum == T:
            cnt += 1
            return
        return
    else :
        for i in range(many_li[v]+1) :
            DFS(v+1, ssum+value_li[v]*i)


T = int(input())
k = int(input())
value_li = []
many_li = []
cnt = 0
for i in range(k) :
    a, b = map(int, input().split())
    value_li.append(a)
    many_li.append(b)

DFS(0,0)
print(cnt)





