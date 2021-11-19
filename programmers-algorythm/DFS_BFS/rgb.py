# RGB 거리
import sys

n = int(sys.stdin.readline())
colors = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(colors)
dp = [[0,0,0] for _ in range(n)]
dp[0] = colors[0]

for i in range(1, n):
    # red
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i][0]
    # green
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i][1]
    # blue
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + colors[i][2]


# print(dp)
print(min(dp[-1]))



# print("시간 :", time.time() - start)