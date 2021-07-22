# 나이트의 이동

import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    length = int(sys.stdin.readline())
    loca_x, loca_y = map(int, sys.stdin.readline().split())
    dest_x, dest_y = map(int, sys.stdin.readline().split())
    # print(length, "!!!")
    # print(loca_x, loca_y)
    # print(dest_x, dest_y)
    dq = deque()
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    ch = [[0]*length for _ in range(length)]
    ch[loca_x][loca_y] = 1
    dq.append((loca_x,loca_y))
    while dq:
        for _ in range(len(dq)):
            tmp_x, tmp_y = dq.popleft()
            if dest_x == tmp_x and dest_y == tmp_y:
                print(ch[dest_x][dest_y]-1)
                dq.clear()
                break
            for i in range(8):
                # print(i)
                x = tmp_x + dx[i]
                y = tmp_y + dy[i]
                if 0<=x<length and 0<=y<length and ch[x][y]==0:
                    ch[x][y] = ch[tmp_x][tmp_y] + 1
                    dq.append((x,y))



