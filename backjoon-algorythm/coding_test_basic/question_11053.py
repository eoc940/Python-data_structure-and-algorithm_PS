# 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
#print(nums)

dp = [0]*n
dp[0] = 1
for i in range(1,n):
    _max = 0
    for j in range(i):
        if nums[i] > nums[j] :
            _max = max(_max, dp[j])
    dp[i] = _max+1
print(max(dp))




