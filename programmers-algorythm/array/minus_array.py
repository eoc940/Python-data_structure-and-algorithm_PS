# 대칭 차집합

import sys

a_leng, b_leng = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort()

a_idx = 0
b_idx = 0
count = 0
while a_idx < a_leng and b_idx < b_leng:
    if a[a_idx] == b[b_idx]:
        count += 1
        a_idx += 1
        b_idx += 1
    else:
        if a[a_idx] > b[b_idx]:
            b_idx += 1
        else:
            a_idx += 1

print(a_leng + b_leng - 2*count)