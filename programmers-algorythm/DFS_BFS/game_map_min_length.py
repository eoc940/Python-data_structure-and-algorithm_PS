# 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 0
    row, col = len(maps), len(maps[0])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dq = deque()
    dq.append((0,0))

    while dq:
        tx, ty = dq.popleft()
        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]
            if 0<=x<row and 0<=y<col and maps[x][y] == 1:
                maps[x][y] = maps[tx][ty] + 1
                dq.append((x,y))

    if maps[row-1][col-1] == 1:
        return -1
    return maps[row-1][col-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
