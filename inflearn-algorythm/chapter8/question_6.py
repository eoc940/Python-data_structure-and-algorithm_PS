# 최대 선 연결하기

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1

for i in range(2, n+1) :
    val = 0
    for j in range(i-1,0,-1) :
        if nums[i] > nums[j] and dy[j] > val :
           val = dy[j]
    dy[i] = val+1
print(max(dy))


