# 상하좌우

import sys

n = int(sys.stdin.readline())
direction_list = list(sys.stdin.readline().split())
x, y = 1, 1

go = {"R":(0,1), "U":(-1,0), "L":(0,-1), "D":(1,0)}
for direction in direction_list:
    dx, dy = go[direction]
    if 1 <= x + dx <= n and 1 <= y + dy <= n :
        x += dx
        y += dy

print(x, y)