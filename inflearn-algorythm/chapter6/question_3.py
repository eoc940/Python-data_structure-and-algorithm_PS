# 부분집합 구하기(DFS)

'''
def DFS(v) :

    if v==n+1 :
        for i in range(1,n+1) :
            if ch[i] == 1 :
                print(i, end=" ")
        print()
    else:
        ch[v]=1
        DFS(v + 1)
        ch[v]=0
        DFS(v + 1)

n = int(input())
ch = [0]*(n+1)
DFS(1)
'''
# 다시 한번 풀어보기

def DFS(v) :
    if v==n+1:
        # ch의 인덱스를 출력
        for i in range(1,n+1) :
            if ch[i]==1 :
                print(i, end=" ")
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

n = int(input())
ch = [0]*(n+1)
DFS(1)














