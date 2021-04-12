# 최대 부분 증가수열
# LIS(Longest Increasing Subsequence)
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1

for i in range(2, n+1) :
    val = 0
    for j in range(i-1, 0, -1) :
        if arr[j] < arr[i] and val < dy[j] :
             val = dy[j]
    dy[i] = val + 1

print(max(dy))

