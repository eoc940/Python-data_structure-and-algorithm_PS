# 가장 먼 노드

# bfs를 이용해 풀어보자

from collections import deque

def solution(n, edge):
    answer = 0
    way = dict()
    for x in edge:
        # 리스트간 더하기 연산 이용
        way[x[0]] = way.get(x[0], [])+ [x[1]]
        way[x[1]] = way.get(x[1], [])+ [x[0]]

    ch = [-1]*(n+1)

    dq = deque()
    dq.append(1)
    ch[1] = 0
    while dq :
        tmp = dq.popleft()
        next_nodes = way[tmp]
        for node in next_nodes :
            if ch[node]==-1 :
                dq.append(node)
                ch[node] = ch[tmp]+1

    maxi_dist = max(ch)

    for i in ch :
        if i==maxi_dist :
            answer+=1

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

