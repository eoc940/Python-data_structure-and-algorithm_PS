# 재귀함수를 이용한 2진수 출력

n = int(input())

def make_eezin(n) :
    if n==0 :
        return
    make_eezin(n//2)
    print(n%2, end="")

make_eezin(n)


# 재귀함수와 스택(선수지식)
'''
def DFS(x) :
    if x>0 :
        DFS(x-1)
        print(x) # 출력부분을 재귀함수 호출부보다 뒤에 선언하면
                 # 역순으로 출력된다

if __name__ == "__main__" :
    n = int(input())
    DFS(n)


# 강사님 풀이

def DFS(x) :
    if x==0:
        return
    else:

        DFS(x//2)
        print(x % 2, end="")

n = int(input())
DFS(n)
'''


# 다시 풀기

def DFS(v) :
    if n==0:
        return
    else:
        DFS(v//2)
        print(v%2 , end=" ")


n = int(input())
DFS(n)


























