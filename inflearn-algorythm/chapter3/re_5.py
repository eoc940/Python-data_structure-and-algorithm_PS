# 수들의 합

import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0

lt = 0
rt = 0

while True :
    if rt == len(nums) :
        break
    if sum(nums[lt:rt+1]) < m :
        rt += 1
    elif sum(nums[lt:rt+1]) == m :
        answer += 1
        lt += 1
    elif sum(nums[lt:rt+1]) > m:
        lt += 1

print(answer)

