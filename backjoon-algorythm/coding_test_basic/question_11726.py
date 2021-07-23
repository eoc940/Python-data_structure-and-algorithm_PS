# 2 * n 타일링

import sys

n = int(sys.stdin.readline())
dp = [0]*(n+2)
dp[1] = 1
dp[2] = 2
for i in range(1,n):
    dp[i+2] = dp[i+1] + dp[i]
#print(dp)
print(dp[n]%10007)


# dp[n]을 구해야 한다




