# 최대힙

import heapq
import sys

num = []

while True :
    n = int(sys.stdin.readline())
    if n==-1 :
        break
    elif n==0 :
        if num :
            print(heapq.heappop(num) * (-1))
        else :
            print(-1)
    else :
        heapq.heappush(num,-n)




