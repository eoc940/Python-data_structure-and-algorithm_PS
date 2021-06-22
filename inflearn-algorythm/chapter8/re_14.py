# 회장뽑기(플로이드 워셜 응용)

import sys

n = int(sys.stdin.readline())
connect = [[float('inf')]*(n+1) for _ in range(n+1)]

while True:
    p1, p2 = map(int, sys.stdin.readline().split())
    if p1 == -1 and p2 == -1 :
        break
    connect[p1][p2] = 1
    connect[p2][p1] = 1

# for x in connect:
#     print(x)

for i in range(1,n+1):
    connect[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            connect[i][j] = min(connect[i][j], connect[i][k] + connect[k][j])

# for x in connect:
#     print(x)
answer = dict()
for i in range(1,n+1):
    answer[i] = max(connect[i][1:])

#print(answer)
score = min(answer.values())
candidate = []
for i,v in answer.items():
    if v==score:
        candidate.append(i)

print(score, len(candidate))
for x in candidate:
    print(x, end=" ")




