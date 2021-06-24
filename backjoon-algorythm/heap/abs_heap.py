# 절대값 힙

import sys, heapq

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

li = []

for x in nums :
    if x == 0 :
        if len(li) == 0:
            print(0)
        else:
            print(heapq.heappop(li)[1])
    else :
        heapq.heappush(li, (abs(x), x))