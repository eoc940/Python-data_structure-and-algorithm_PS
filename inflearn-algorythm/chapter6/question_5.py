# 바둑이 승차(DFS)
'''
def DFS(v, sum) :
    if sum > C :
        return
    if v==n:
        global result # 전역변수를 지역범위에서 사용하고 싶을때 global을 쓴다
        if sum > result :
            result = sum
    else:
        DFS(v+1, sum + a[v])
        DFS(v+1, sum)


C, n = map(int, input().split())
a = [int(input()) for _ in range(n)]
result = 0
DFS(0, 0)
print(result)

# 잠깐지식(전역변수와 지역변수)

def DFS1():
    cnt = 3
    print(cnt)

cnt가 자기의 지역변수인지 확인해보고
만약 cnt가 지역변수가 아니라면 전역변수인지 확인한다
즉 함수는 지역변수가 우선이다.
'''
'''

def DFS2():
    global cnt # 이러면 에러가 나지않는다. cnt는 전역변수라는 의미다
    if cnt==5:
        cnt=cnt+1 # 좌변 cnt은 지역변수를 만든다는 의미다 그래서 에러난다
        print(cnt)

def DFS3():
    a = a + [4] # 이렇게 쓰면 a는 로컬이기 때문에 에러가 뜬다. 해결하려면 global붙인다
    a[0] = 7 # 리스트의 경우는 로컬을 만드는게 아니라 전역리스트를 그대로 사용
    print(a)

if __name__ == "__main__":
    cnt = 5 # 변수 생성, 값 할당
    a = [1,2,3]
    DFS1()
    DFS2()
    DFS3()
    print(cnt)
'''

# 강사님 풀이

def DFS(L, sum, tsum) :
    global result
    if sum+(total-tsum) < result:
        return
    if sum > c:
        return
    if L==n:
        if sum > result:
            result = sum # 할당하고 있기 때문에 result는 로컬
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

c, n = map(int, input().split())
a = [0]*n
result = -2147000000
for i in range(n) :
    a[i] = int(input())
total = sum(a)
DFS(0,0,0)
print(result)


