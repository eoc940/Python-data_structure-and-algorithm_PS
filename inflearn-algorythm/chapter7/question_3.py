# 양팔저울(DFS)

# 교훈!!
# 리스트에서 remove연산하는 것보다
# set을 따로 만들어서 list와 비교하는 것이
# 연산속도가 빠르다!!!
'''
def DFS(v, sum) :
    global res
    ######### 1 #########
    # if v==k and sum in s:
    #     s.remove(sum)
    #     return
    # if v==k :
    #     return
    ######### 2 #########
    if v==k:
        if 0<sum<=tot:
            res.add(sum)

    ##################
    else :
        DFS(v+1, sum + w[v])
        DFS(v+1, sum - w[v])
        DFS(v+1, sum)

k = int(input())
w = list(map(int, input().split())) # 추 리스트
tot = sum(w)
s = [x for x in range(1, sum(w)+1)] # 1부터 sum(추) 리스트
res = set()
DFS(0,0)
####### 1 #######
# print(len(s))
####### 2 #######
print(sum(w) - len(res))
'''







# 다시풀기

def DFS(L, sum) :
    if L==k:
        if 0 < sum <= s :
            possible.add(sum)
        return
    else :
        DFS(L+1, sum + weight[L])
        DFS(L+1, sum - weight[L])
        DFS(L+1, sum)

k = int(input())
weight = list(map(int, input().split()))
possible = set()
s = sum(weight)
DFS(0, 0)
print(s - len(possible))





















