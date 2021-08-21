# 1로 만들기

import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[1] = 0
dp[2] = min(dp[1], dp[1]) + 1
dp[3] = min(dp[2], dp[1]) + 1
dp[4] = min(dp[3], dp[2]) + 1
dp[5] = min(dp[4], dp[1]) + 1

if n <= 5:
    print(dp[n])
else :
    for i in range(6, n+1):
        possible = [dp[i-1]]
        if i%5 == 0: possible.append(dp[i//5])
        elif i%3 == 0: possible.append(dp[i//3])
        elif i%2 == 0: possible.append(dp[i//2])
        dp[i] = min(possible) + 1
    print(dp)
    print(dp[n])