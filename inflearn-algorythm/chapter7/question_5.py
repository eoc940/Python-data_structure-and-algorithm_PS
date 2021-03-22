# 동전 분배하기(DFS)


def DFS(v, A,B,C) :
    global res
    if v==n :
        if A!=B and B!=C and C!=A :
            if res > max(A,B,C)-min(A,B,C) :
                res = max(A,B,C)-min(A,B,C)

    else :
        DFS(v+1, A+coin_li[v],B ,C)
        DFS(v+1, A, B+coin_li[v],C)
        DFS(v+1, A, B, C+coin_li[v])


n = int(input())
coin_li = [int(input()) for _ in range(n)]
res = float('inf')
DFS(0,0,0,0)
print(res)

# 강사님 풀이

def DFS(L) :
    global res
    if L==n :
        cha = max(money)-min(money)
        if cha<res:
            tmp = set()
            for x in money :
                tmp.add(x)
            if len(tmp) == 3:
                res=cha
    else:
        for i in range(3) :
            money[i]+=coin_li[L]
            DFS(L+1)
            money[i]-=coin_li[L]


n = int(input())
coin_li = [int(input()) for _ in range(n)]
money = [0]*3
res = float('inf')
DFS(0)
print(res)
