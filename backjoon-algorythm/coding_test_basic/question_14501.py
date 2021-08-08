# 퇴사

import sys

n = int(sys.stdin.readline())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
schedule.insert(0, [0,0])
print(schedule)
dp = [0]*(n+1)

# # dp[x]의 의미는 x일까지 끝나는 금액의 최대값
# for i in range(n):
#     for j in range(i+schedule[i][0], n+1):
#         dp[j] += schedule[i][1]
#     print(dp)


'''
def dfs(day,tot):
    global answer
    if day > n:
        return
    if day==n:
        answer = max(tot, answer)
    else:
        dfs(day + schedule[day][0], tot + schedule[day][1])
        dfs(day + 1, tot)

answer = float('-inf')
dfs(0,0)
print(answer)
'''