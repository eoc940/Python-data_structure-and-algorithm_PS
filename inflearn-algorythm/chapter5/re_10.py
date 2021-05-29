# 최소힙

import heapq
import sys

nums = []
#heapq.heapify(nums)

while True :
    n = int(sys.stdin.readline())
    if n == -1 :
        break
    elif n == 0 :
        print(heapq.heappop(nums))
    else :
        heapq.heappush(nums, n)


