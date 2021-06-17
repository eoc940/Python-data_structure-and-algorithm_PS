# 직각다각형

import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())

line = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count_x = defaultdict(int)
count_y = defaultdict(int)
flag = False

if line[0][0] == line[1][0] :
    flag = True
else :
    last = line.pop()
    line.insert(0,last)
for i in range(len(line)-1):
    x_maxi = max(line[i-1][0], line[i][0])
    x_mini = min(line[i-1][0], line[i][0])
    y_maxi = max(line[i][1], line[i+1][1])
    y_mini = min(line[i][1], line[i+1][1])
    x_total, y_total = 0, 0
    for a in range(x_mini, x_maxi) :
        count_x[a+0.5] += 1
    for b in range(y_mini, y_maxi) :
        count_y[b+0.5] += 1

#print(count_x)
#print(count_y)
answer = max(max(count_x.values()), max(count_y.values()))
print(answer)
