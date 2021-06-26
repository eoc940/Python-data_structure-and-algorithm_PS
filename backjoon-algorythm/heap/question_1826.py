# 연료 채우기

import sys, heapq
from collections import deque

n = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
desti, fuel = map(int, sys.stdin.readline().split())

info.sort()
#info = deque(info) # while문으로 하는 방법

cnt = 0
idx = 0 # for문으로 하는 방법
station = []
while fuel < desti:

    # while info :
    #     loca, fuel_quan = info.popleft()
    #     if loca <= fuel :
    #         heapq.heappush(station, -1 * fuel_quan)
    #     else:
    #         info.appendleft([loca, fuel_quan])
    #         break

    for i in range(idx, len(info)):
        loca, fuel_quan = info[i][0], info[i][1]
        if loca <= fuel :
            heapq.heappush(station, -1 * fuel_quan)
        else :
            idx = i
            break

    try :
        fuel += heapq.heappop(station)*(-1)
        cnt += 1
    except :
        cnt = -1
        break

print(cnt)




