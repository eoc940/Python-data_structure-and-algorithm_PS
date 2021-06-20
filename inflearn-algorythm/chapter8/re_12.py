# 최대점수 구하기(냅색 알고리즘)

import sys

n,m = map(int, sys.stdin.readline().split())
quest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
'''
dp = [0]*(m+1)

for val, time in quest:
    for i in range(m, time-1, -1):
        dp[i] = max(dp[i], dp[i-time] + val)
    #print(dp)
print(dp[-1])
'''
def dfs(v, total, time):
    global answer
    if time > m :
        return
    if v==n:
        if total > answer and time <= m:
            answer = total
    else :
        dfs(v+1, total + quest[v][0], time + quest[v][1])
        dfs(v+1, total, time)

answer = 0
dfs(0,0,0)
print(answer)





