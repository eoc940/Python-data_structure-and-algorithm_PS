# 중량제한

import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
island_st, island_en = map(int, sys.stdin.readline().split())

connect = defaultdict(list)
for st, en, wei in info:
    connect[st].append((en, wei))
    connect[en].append((st, wei))
print(connect)

def bfs(wei, st):
    dq = deque()
    ch[st] = 1
    dq.append(st)
    flag = False
    while dq and not flag:
        tmp = dq.popleft()
        for node, w in connect[tmp]:
            if ch[node] == 0 and wei <= w:
                ch[node] = 1
                dq.append(node)
                if node == island_en:
                    flag = True
                    break
    return flag


lt = 0
rt = 1000000000
answer = 0
while lt <= rt:
    ch = [0] * (n + 1)
    mid = (lt+rt)//2
    if bfs(mid, island_st): # 해당 무게로 돌 수 있는 경우
        lt = mid + 1
        answer = mid
    else : # 해당 무게로 돌 수 없는 경우
        rt = mid - 1

print(answer)



