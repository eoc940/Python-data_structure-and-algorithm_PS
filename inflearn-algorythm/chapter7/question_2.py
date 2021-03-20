# 휴가(삼성 sw역량평가 기출문제 : DFS활용)

def DFS(L, price) :
    global res
    if L==n+1:
        if price > res:
            res = price
    else :
        if L+time_list[L] <= n+1 :
            DFS(L+time_list[L], price+price_list[L])
        DFS(L + 1, price)

n = int(input())
time_list = []
price_list = []
res = 0
for i in range(n) :
    a, b = map(int, input().split())
    time_list.append(a)
    price_list.append(b)
time_list.insert(0,0)
price_list.insert(0,0)
DFS(1,0)
print(res)

#################################################
def DFS(L, price) :
    global res
    if L==n:
        if price > res:
            res = price
    else :
        if L+time_list[L] <= n :
            DFS(L+time_list[L], price+price_list[L])

        DFS(L + 1, price)

n = int(input())
time_list = []
price_list = []
res = 0
for i in range(n) :
    a, b = map(int, input().split())
    time_list.append(a)
    price_list.append(b)

DFS(0,0)
print(res)

