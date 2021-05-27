# 회의실 배정(그리디)

import sys

n = int(sys.stdin.readline())
time = []
for i in range(n) :
    std, end = map(int, sys.stdin.readline().split())
    time.append((std,end))

time.sort(key=lambda x : (x[1],x[0]))

count = 0
locate = 0
for x in time :
    if x[0] >= locate :
        locate = x[1]
        count += 1


print(count)

