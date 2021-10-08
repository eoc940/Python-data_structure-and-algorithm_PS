# 네트워크

def dfs(node, computers, ch):
    ch[node] = 1
    for i, val in enumerate(computers[node]):
        if node != i and val == 1 and ch[i] == 0:
            dfs(i, computers, ch)


def solution(n, computers):
    answer = 0
    ch = [0 for _ in range(n)]

    for i in range(n):
        if ch[i] == 0:
            dfs(i, computers, ch)
            answer += 1
    return answer