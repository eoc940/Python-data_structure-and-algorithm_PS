# 순위

def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    for x in results :
        graph[x[0]][x[1]] = 1
        graph[x[1]][x[0]] = 2

    for x in graph :
        print(x)

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))