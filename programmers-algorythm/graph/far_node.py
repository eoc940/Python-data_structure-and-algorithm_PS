# 가장 먼 노드

from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    ch = [-1 for _ in range(n+1)]
    graph = defaultdict(list)
    for stt, end in edge:
        graph[stt].append(end)
        graph[end].append(stt)


    dq = deque()
    dq.append(1)
    ch[1] = 0
    dist = 0
    while dq:
        dist += 1
        for _ in range(len(dq)):
            node = dq.popleft()
            for next in graph[node]:
                if ch[next] == -1:
                    ch[next] = dist
                    dq.append(next)

    # print(ch)
    max_leng = max(ch)

    return ch.count(max_leng)

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
