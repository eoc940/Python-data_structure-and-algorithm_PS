# 공 이동 시뮬레이션

def move(row, col, queries, n, m):
    for direct, dist in queries:
        # 좌로 이동
        if direct == 0:
            for _ in range(dist):
                if col-1 >= 0:
                    col -= 1
        # 우로 이동
        elif direct == 1:
            for _ in range(dist):
                if col+1 <= m-1:
                    col += 1
        # 위로 이동
        elif direct == 2:
            for _ in range(dist):
                if row-1 >= 0:
                    row -= 1
        # 아래로 이동
        else:
            for _ in range(dist):
                if row+1 <= n-1:
                    row += 1
    return row, col


def solution(n, m, x, y, queries):
    answer = 0
    for i in range(n):
        for j in range(m):
            moved_row, moved_col = move(i, j, queries,n,m)
            if moved_row == x and moved_col == y:
                answer += 1
    return answer

n,m,x,y = 2,5,0,1
queries = [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
print(solution(n,m,x,y,queries))