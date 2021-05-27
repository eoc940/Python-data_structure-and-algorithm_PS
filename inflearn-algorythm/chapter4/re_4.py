# 마구간 정하기(결정알고리즘)

import sys

n,c = map(int, sys.stdin.readline().split())
loca = [int(sys.stdin.readline()) for _ in range(n)]

lt = 1
loca.sort()
rt = max(loca)
res = 0
def count(dist) :
    cnt = 1
    location = loca[0]
    for x in loca :
        if x - location >= dist :
            cnt += 1
            location = x
    return cnt

while lt<=rt :

    mid = (lt+rt)//2
    if count(mid) >= c : #c마리 이상 넣을 수 있으면 답이 될 수 있음
        lt = mid + 1 # 최대 거리를 찾아야 하므로 큰 값을 찾을 수 있도록 값 조정
        res = mid
    else :
        rt = mid - 1

print(res)

