# 개미 전사

import sys

n = int(sys.stdin.readline())
eat = list(map(int, sys.stdin.readline().split()))
eat.insert(0,0)

dp = [0]*(n+1)
dp[1] = eat[1]
dp[2] = max(eat[1], eat[2])
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + eat[i], dp[i-1])

print(dp[n])

