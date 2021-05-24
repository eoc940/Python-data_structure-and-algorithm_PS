# 이분검색

import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

lt = 0
rt = len(num)

while lt<=rt :
    mid = (lt + rt) // 2
    if num[mid] == m:
        print(mid + 1)
        break
    if num[mid] > m :
        rt = mid - 1
    else :
        lt = mid + 1



