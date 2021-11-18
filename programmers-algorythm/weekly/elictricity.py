# 전력망을 둘로 나누기

from itertools import combinations
from collections import defaultdict, deque

def solution(n, wires):
    answer = float('inf')
    nodes = set()
    for st, en in wires:
        nodes.add(st)
        nodes.add(en)
    nodes = sorted(list(nodes))
    # print(nodes)
    for link in list(combinations(wires, len(wires)-1)):
        mapp = defaultdict(list)
        for stt, end in link:
            mapp[stt].append(end)
            mapp[end].append(stt)
        ch = [0 for _ in range(len(nodes)+1)]
        dq = deque()
        dq.append(nodes[0])
        cnt = 1
        ch[nodes[0]] = 1
        # bfs
        while dq:
            tmp = dq.popleft()
            for x in mapp[tmp]:
                if ch[x] == 0:
                    ch[x] = 1
                    dq.append(x)
        group_one = sum(ch)
        group_two = len(nodes) - group_one

        if answer > abs(group_one - group_two):
            # print(group_one, group_two)
            answer = abs(group_one - group_two)

    return answer


n = 4
wires = [[1,2],[2,3],[3,4]]
print(solution(n,wires))