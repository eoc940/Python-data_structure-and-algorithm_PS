# 휴가(삼성 sw역량평가 기출문제 : DFS활용)
'''
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
'''

# 다시 풀기



def DFS(L, sum) :
    global res
    if L==n+1 :
        if sum > res :
            res = sum
    else :
        if L+time_li[L] <= n+1 :
        # 해당 날짜를 get하고 기한 이후 DFS 호출
            DFS(L+time_li[L], sum + point_li[L])
        # 해당 날짜를 not get하고 하루 넘김
        DFS(L+1, sum)

n = int(input())
time_li = []
point_li = []
res = 0
for i in range(n) :
    a, b =map(int, input().split())
    time_li.append(a)
    point_li.append(b)
# 두 리스트는 인덱스 1부터 값이 들어가있음
time_li.insert(0,0)
point_li.insert(0,0)
DFS(1,0)

print(res)






