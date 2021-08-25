# 병사 배치하기

import sys

n = int(sys.stdin.readline())
power = list(map(int, sys.stdin.readline().split()))
dp = [1]*len(power)

for i in range(1, len(dp)):
    if power[i-1] > power[i]:
        dp[i] = max(dp[i-1] + 1, dp[i])
    else :
        dp[i] = dp[i-1]
print(dp)
print(dp[-1])

'''
answer = 0
for i in range(1, len(power)):
    if power[i-1] < power[i]:
        answer += 1
print(answer)
'''





