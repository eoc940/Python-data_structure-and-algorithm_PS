# 역수열

import sys

n= int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n,0,-1) :
    answer.insert(nums[i-1], i)

for x in answer :
    print(x, end=" ")






