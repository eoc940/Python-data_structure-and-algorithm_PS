# 회장뽑기(플로이드 워셜 응용)

import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
connect = defaultdict(list)

while True:
    p1, p2 = map(int, sys.stdin.readline().split())
    if p1 == -1 and p2 == -1 :
        break
    connect[p1].append(p2)
    connect[p2].append(p1)

#print(connect)

def bfs(candi) :
    ch = [0]*(n+1)
    dq = deque()
    ch[candi] = 1
    dq.append(candi)
    cnt = 0
    while dq :
        for _ in range(len(dq)):
            tmp = dq.popleft()
            for friend in connect[tmp]:
                if ch[friend]==0:
                    ch[friend] = 1
                    dq.append(friend)
        cnt += 1
        if sum(ch) == n:
            break
    return cnt


relation_dist = dict()
for i in range(1,n+1):
    relation_dist[i] = bfs(i)
#print(relation_dist)

score = min(relation_dist.values())
candidate = []
for i,v in relation_dist.items():
    if v==score:
        candidate.append(i)
print(score, len(candidate))
for x in candidate:
    print(x, end=" ")






'''
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
'''



