# 떡볶이 떡 만들기

import sys

n,m = map(int, sys.stdin.readline().split())
rice = list(map(int, sys.stdin.readline().split()))
answer = 0
lt, rt = 0, max(rice)

def rice_quantity(mid):
    total = 0
    for x in rice:
        length = x - mid
        if length > 0 : total += length
    return total

while lt <= rt:
    mid = (lt + rt) // 2
    if rice_quantity(mid) >= m:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)



