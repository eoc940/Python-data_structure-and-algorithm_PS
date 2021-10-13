# N-Queen

def check(row, col, locations):
    for row_prior, col_prior in locations:
        if abs(row_prior-row) == abs(col_prior-col):
            return False
    return True

def dfs(L, ch, n, locations):
    global answer
    if L == n:
        # print(locations)
        answer += 1
    else:
        for i in range(n):
            if ch[i] == 0 and check(L, i, locations):
                ch[i] = 1
                locations.append([L, i])
                dfs(L+1, ch, n, locations)
                locations.pop()
                ch[i] = 0

def solution(n):
    global answer
    answer = 0
    ch = [0 for _ in range(n)]
    dfs(0, ch, n, [])

    return answer

n = 5
print(solution(n))