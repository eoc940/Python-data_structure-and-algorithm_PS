# 강의실 배정

import sys, heapq

n = int(sys.stdin.readline())

time = []

for _ in range(n):
    heapq.heappush(time, list(map(int,sys.stdin.readline().split())))

answer = []
st, en = heapq.heappop(time)
answer.append(en)

while time:
    st, en = heapq.heappop(time)
    criteria = heapq.heappop(answer)
    if criteria <= st:
        heapq.heappush(answer, en)
    else:
        heapq.heappush(answer, criteria)
        heapq.heappush(answer, en)
    #print(answer)
print(len(answer))







