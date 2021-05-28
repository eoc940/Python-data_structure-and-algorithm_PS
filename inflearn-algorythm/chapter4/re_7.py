# 창고 정리

import sys
import heapq

L = int(sys.stdin.readline())
hei = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

for i in range(m) :
    # 최대값 구하기
    heapq.heapify(hei)
    tmp = []
    for x in hei :
        heapq.heappush(tmp, (-x, x))

    #print("변경전 :", hei, end=" ")
    maxi = tmp[0][1]
    #print(maxi, end=' ')

    hei.remove(maxi)
    heapq.heappush(hei, maxi-1)

    mini = heapq.heappop(hei)
    heapq.heappush(hei, mini+1)
    #print("변경후 :", hei)
print(max(hei) - hei[0])




