

def solution(n, start, end, roads, traps):
    answer = 0
    way = [[4000]*(n+1) for _ in range(n+1)]
    for i in roads :
        beg= i[0]
        fin = i[1]
        dist = i[2]
        way[beg][fin] = dist
    for i in range(1, n+1):
        way[i][i] = 0
    print(way)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                way[i][j] = min(way[i][j], way[i][k] + way[k][j])
                if k in traps :
                    print(way, "?")
                    for i in range(1, n+1):
                        for j in range(i, n + 1):
                            way[i][j], way[j][i] = way[j][i], way[i][j]
                    print(way, "$")
    answer = way[start][end]
    return answer

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
