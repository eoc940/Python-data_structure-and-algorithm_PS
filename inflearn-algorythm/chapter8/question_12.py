# 최대점수 구하기(냅색 알고리즘)
'''
import sys

n, m = map(int, sys.stdin.readline().split())
questions = []
for _ in range(n) :
    score, time = map(int, sys.stdin.readline().split())
    questions.append((score,time))
questions.insert(0, (0,0))

#dy를 2차원 리스트로 한 이유는 한 문제밖에 풀 수 없기 때문이다.
dy = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1) :
    ps = questions[i][0]
    pt = questions[i][1]
    for k in range(pt) :
        dy[i][k] = dy[i-1][k]
    for j in range(pt, m+1) :
        #위의 값과 비교해서 클때는 업데이트
        if dy[i-1][j] > dy[i-1][j-pt] + ps :
            dy[i][j] = dy[i-1][j]
        else :
            dy[i][j] = dy[i-1][j-pt] + ps

print(dy[n][m])
'''
#강사님 풀이... dy를 1차원으로 표현함
#뒤쪽 인덱스부터 dy를 채울 수도 있다는 걸 알자!!
import sys

n, m = map(int, sys.stdin.readline().split())
questions = []
for _ in range(n) :
    score, time = map(int, sys.stdin.readline().split())
    questions.append((score,time))
questions.insert(0, (0,0))

dy = [0]*(m+1)
for i in range(1, n+1) :
    ps = questions[i][0]
    pt = questions[i][1]
    for j in range(m, pt-1, -1) :
        if dy[j] < dy[j-pt]+ps :
            dy[j] = dy[j-pt]+ps

print(dy[m])
