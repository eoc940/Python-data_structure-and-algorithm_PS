# 연속합

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = nums[0]


for i in range(1,n):
    dp[i] = max(nums[i], dp[i-1]+nums[i])
print(max(dp))



