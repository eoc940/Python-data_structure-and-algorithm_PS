# 가장 높은 탑 쌓기

import sys

n = int(sys.stdin.readline())
block = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

block.sort(reverse=True)
dp = [0]*n

dp[0] = block[0][1]

for i in range(1,n) :
    _max = 0
    for j in range(i-1,-1,-1):
        if block[i][2] < block[j][2] and _max < dp[j]:
            _max = dp[j]
    dp[i] = _max + block[i][1]
print(max(dp))








