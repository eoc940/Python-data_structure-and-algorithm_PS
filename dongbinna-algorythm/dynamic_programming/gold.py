# 금광

import sys

iterate = int(sys.stdin.readline())

for _ in range(iterate):
    n,m = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    golds = [li[i:i+m] for i in range(0, len(li), m)]
    for x in golds:
        print(x)
    print()
    answer = 0
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = golds[i][0]

    for i in range(1, m):
        for j in range(n):
            # j-1, j, j+1  i-1
            for k in range(j-1, j+2):
                if 0<=k<n:
                    dp[j][i] = max(dp[k][i-1]+golds[j][i], dp[j][i])
                    answer = max(answer, dp[j][i])
    for x in dp:
        print(x)
    print(answer)