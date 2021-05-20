# 가장 먼 노드

# bfs를 이용해 풀어보자

from collections import deque

def solution(n, edge):
    answer = 0
    way = dict()
    # way에 양방향 노드,거리정보 넣어줌
    for x in edge:
        way[x[0]] = way.get(x[0], [])+ [x[1]]
        way[x[1]] = way.get(x[1], [])+ [x[0]]

    # 노드 지났는지 정보와 거리 정보를 담을 ch 생성, bfs를 위한 deque생성
    ch = [-1]*(n+1)
    dq = deque()
    dq.append(1)
    ch[1] = 0

    # bfs를 통해 ch에 거리 정보 담기
    while dq :
        tmp = dq.popleft()
        next_nodes = way[tmp]
        for node in next_nodes :
            if ch[node]==-1 :
                dq.append(node)
                ch[node] = ch[tmp]+1

    # ch의 최대값(초기노드로부터의 거리 최대값)을 maxi_dist에 저장
    maxi_dist = max(ch)

    # 최대값과 일치하면 1증가
    for i in ch :
        if i==maxi_dist :
            answer+=1

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

