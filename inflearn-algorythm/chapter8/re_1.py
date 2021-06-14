# 동적계획법이란? 네트워크 선 자르기(Bottom-Up)

import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)

dp[1] = 1
dp[2] = 2
for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])




