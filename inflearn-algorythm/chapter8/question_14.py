# 회장 뽑기(플로이드 워셜 응용)

import sys

n = int(sys.stdin.readline())
friend = [[100]*(n+1) for _ in range(n+1)]

for i in range(1,n+1) :
    friend[i][i] = 0

while(True) :
    f1, f2 = map(int, sys.stdin.readline().split())
    if f1 == -1 and f2 == -1 :
        break
    friend[f1][f2] = 1
    friend[f2][f1] = 1

# 플로이드 워셜 알고리즘
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])

score = 100

for i in range(n+1) :
    friend[i][0] = 0
#각 행의 최대끼리 비교하여 최소값을 찾아 score에 저장
for i in range(1,n+1) :
    score = min(score, max(friend[i]))

res = []
#score와 일치하는 각 행 최댓값을 갖는 i를 리스트에 저장
for i in range(1,n+1) :
    if max(friend[i])==score :
        res.append(i)

print(score, len(res))
for x in res :
    print(x, end=" ")


