# 네트워크 선 자르기(top-down : 재귀, 메모이제이션)
'''
메모이제이션은 기록을 하여 다음번 호출이 발생했을 때
불필요한 호출을 방지한다.
'''
import sys

def D(v) :
    global total
    if dy[v] != 0 :
        total += dy[v]
    elif v>=3 :
        D(v-1)
        D(v-2)

n = int(sys.stdin.readline())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
total = 0
D(7)
print(total)

# 강사님 풀이

def DFS(len) :
    # 가지 컷팅(메모이제이션)
    if dy[len]>0:
        return dy[len]

    if len==1 or len==2 :
        return len
    else :
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

n = int(sys.stdin.readline())
dy = [0]*(n+1)
print(DFS(n))