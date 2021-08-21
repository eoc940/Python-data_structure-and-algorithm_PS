# 효율적인 화폐 구성

import sys

n,m = map(int, sys.stdin.readline().split())
currency = [int(sys.stdin.readline()) for _ in range(n)]
currency.sort()

dp = [float('inf')]*(m+1)
dp[0] = 0
for value in currency:
    # dp[value] = 1
    for i in range(value, m+1, value):
        dp[i] = min(dp[i-value]+1, dp[i])


print(dp)
if dp[m] == 0: print(-1)
else : print(dp[m])
