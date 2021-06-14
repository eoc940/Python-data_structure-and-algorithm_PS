# 최대 선 연결하기

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0]*n

dp[0] = 1

for i in range(1, n) :
    _max = 0
    for j in range(i-1,0,-1) :
        if nums[i] > nums[j] and dp[j] > _max:
            _max = dp[j]
    dp[i] = _max+1

print(max(dp))



