# 배달

def solution(N, road, K):
    answer = 0
    way = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

    #way에 road의 값들을 넣기
    for r in road :

        node1, node2, dist = r[0], r[1], r[2]

        #이미 node1->node2 값이 들어가 있을때 비교하여 최소값을 넣어줌
        if way[node1][node2] != float('inf') :
            way[node1][node2] = min(dist, way[node1][node2])
            way[node2][node1] = min(dist, way[node1][node2])

        #값이 들어가있지 않다면 그대로 넣어줌
        else :
            way[node1][node2] = dist
            way[node2][node1] = dist

    #자기자신으로 가는 거리는 0으로 초기화
    for i in range(N+1) :
        way[i][i] = 0

    #플로이드 워셜 알고리즘
    for path in range(1, N+1) :
        for i in range(1, N+1) :
            for j in range(1, N+1) :
                if way[i][path]+way[path][j] < way[i][j] :
                    way[i][j] = way[i][path]+way[path][j]
    #개수 세주기
    for x in range(1,N+1) :
        if way[1][x] <= K :
            answer += 1

    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))