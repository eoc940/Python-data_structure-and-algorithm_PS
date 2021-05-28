# 침몰하는 타이타닉(그리디)

import sys

n,m = map(int, sys.stdin.readline().split())

weight = list(map(int, sys.stdin.readline().split()))
weight.sort()

left_cur = 0
right_cur = len(weight)-1
boat = 0

while left_cur <= right_cur :
    if weight[left_cur] + weight[right_cur] <= m :
        left_cur += 1
        right_cur -= 1
        boat += 1

    else :
        right_cur -= 1
        boat += 1

print(boat)

