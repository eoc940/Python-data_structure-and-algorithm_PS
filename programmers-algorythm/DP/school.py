# 등굣길

def solution(m, n, puddles):
    answer = 0
    _map = [[0]*m for _ in range(n)]
    for x, y in puddles:
        _map[y-1][x-1] = -1
    # for x in _map:
    #     print(x)
    # print()
    for i in range(1,m):
        if _map[0][i] == 0:
            _map[0][i] = 1
        else:
            break
    # for x in _map:
    #     print(x)
    # print()
    for i in range(1,n):
        if _map[i][0] == 0:
            _map[i][0] = 1
        else:
            break
    # for x in _map:
    #     print(x)
    # print()
    for i in range(1,n):
        for j in range(1,m):
            if _map[i][j] == -1:
                continue
            if _map[i-1][j] > 0:
                _map[i][j] += _map[i-1][j]
            if _map[i][j-1] > 0 :
                _map[i][j] += _map[i][j-1]

    # for x in _map:
    #     print(x)

    return _map[n-1][m-1]%1000000007

m = 4
n = 3
puddles= [[2,2],[4,1]]

print(solution(m,n,puddles))