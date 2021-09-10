# 합승 택시 요금

INF = 40000000

def floyd(dist, n):

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

def solution(n, s, a, b, fares):
    answer = INF
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2]
        dist[edge[1]-1][edge[0]-1] = edge[2]

    floyd(dist, n)
    # for x in distance:
    #     print(x)

    for i in range(n):
        answer = min(answer, dist[s-1][i] + dist[i][a-1] + dist[i][b-1])

    return answer

n,s,a,b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))