# 동전교환

import sys

n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))
change = int(sys.stdin.readline())

dp = [float('inf')]*(change+1)
dp[0] = 0
for val in coin:
    for i in range(val, change+1):
        dp[i] = min(dp[i-val]+1, dp[i])
    #print(dp)
print(dp[-1])







