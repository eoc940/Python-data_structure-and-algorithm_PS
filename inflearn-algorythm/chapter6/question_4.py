# 합이 같은 부분집합(DFS : 아마존 인터뷰)

import sys

def DFS(v) :
    if v==n:
        # ch값에 따른 두 리스트 합을 비교하여 결과 도출
        first_list.clear()
        secound_list.clear()
        for i in range(len(a)) :
            if ch[i] == 1:
                first_list.append(a[i])
            else :
                secound_list.append(a[i])
        if sum(first_list) == sum(secound_list) :
            result.append(True)
        else :
            result.append(False)
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


n = int(input())
a = list(map(int, input().split()))
ch = [0] * n
first_list = list()
secound_list = list()
result = []
DFS(0)
if True in result :
    print("YES")
else :
    print("NO")

# 강사님 풀이

def DFS(L, sum) : # L은 인덱스 번호, sum은 누적값
    if sum > total//2 :
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

n = int(input())
a = list(map(int, input().split()))
total = sum(a)
DFS(0,0)
print("NO")

