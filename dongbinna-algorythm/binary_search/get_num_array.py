# 정렬된 배열에서 특정 수의 개수 구하기

import sys

n,x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

lt, rt = 0, len(nums)-1
left, right = 0, 0

while lt <= rt:
    mid = (lt + rt) // 2
    if nums[mid] == x:
        lt = mid + 1
        right = mid
    else:
        rt = mid - 1

lt, rt = 0, len(nums)-1

while lt <= rt:
    mid = (lt + rt) // 2
    if nums[mid] == x:
        rt = mid - 1
        left = mid
    else:
        lt = mid + 1

print(right-left+1)
