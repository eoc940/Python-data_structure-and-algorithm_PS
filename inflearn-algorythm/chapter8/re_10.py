# 가방 문제(냅색 알고리즘)

import sys

n, _max = map(int, sys.stdin.readline().split())
info = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
info.sort()
#print(info)

dp = [0]*(_max+1)
for i,v in enumerate(info):
    wei, val = v[0], v[1]
    for j in range(wei, _max+1):
        if dp[j-wei] + val > dp[j]:
            dp[j] = dp[j-wei] + val
    #print(dp)
print(dp[-1])





