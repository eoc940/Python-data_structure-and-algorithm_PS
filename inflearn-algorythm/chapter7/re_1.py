# 최대점수 구하기(dfs)
# 이 문제의 아이디어는 인덱스를 넘어가면서 이 문제 푸는경우, 안푸는경우 두개로 나누는 것이다
import sys

n, m = map(int, sys.stdin.readline().split())

quiz = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(quiz)
def dfs(v, time, score) :
    global _max
    if time > m :
        return
    if v==n :
        if score > _max :
            _max = score
    else :
        dfs(v+1, time+quiz[v][1], score+quiz[v][0])
        dfs(v+1, time, score)


ch = [0]*n
_max = 0
dfs(0,0,0)
print(_max)





