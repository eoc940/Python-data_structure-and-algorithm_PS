# 알리바바와 40인의 도둑

import sys

n = int(sys.stdin.readline())
rock = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = rock[0][0]
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + rock[i][0]
    dp[0][i] = dp[0][i-1] + rock[0][i]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + rock[i][j]

print(dp[n-1][n-1])

