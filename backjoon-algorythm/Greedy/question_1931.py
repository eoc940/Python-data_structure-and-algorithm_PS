# 회의실 배정

import sys

n = int(sys.stdin.readline())
time_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

count = 0
time_table.sort(key=lambda x : (x[1],x[0]))
end_time = -1
#print(time_table)

for i, v in enumerate(time_table):
    if v[1] >= end_time and v[0] >= end_time :
        end_time = v[1]
        count += 1

print(count)


