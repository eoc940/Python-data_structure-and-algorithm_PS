# 직각다각형

import sys
from collections import defaultdict

n = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.append(data[0])

num_dict_x = defaultdict(int)
num_dict_y = defaultdict(int)

pre_x, pre_y = data[0][0], data[0][1]
for i in range(1, len(data)):
    x,y = data[i][0], data[i][1]
    if x==pre_x :
        start = min(y,pre_y)
        end = max(y,pre_y)
        num_dict_y[start] += 1
        num_dict_y[end] -= 1

    if y==pre_y:
        start = min(x,pre_x)
        end = max(x,pre_x)
        num_dict_x[start] += 1
        num_dict_x[end] -= 1

    pre_x, pre_y = x, y
# print(num_dict_x)
# print(num_dict_y)
num_dict_x = sorted(num_dict_x.items(), key=(lambda x:x[0]))
num_dict_y = sorted(num_dict_y.items(), key=(lambda x:x[0]))
# print(num_dict_x)
# print(num_dict_y)

max_x = 0
tmp_x = 0
for k, v in num_dict_x:
    tmp_x += v
    max_x = max(max_x, tmp_x)

max_y = 0
tmp_y = 0
for k, v in num_dict_y:
    tmp_y += v
    max_y = max(max_y, tmp_y)

print(max(max_x, max_y))