# 뮤직비디오(결정알고리즘)

import sys

n, m = map(int, sys.stdin.readline().split())
song = list(map(int, sys.stdin.readline().split()))

def count(val) :
    cnt = 1
    total = 0
    for x in song :
        if total + x > val :
            cnt += 1
            total = x
        else :
            total += x
    return cnt

lt = 1
rt = sum(song)
res = 0

while lt<=rt :
    mid = (lt+rt)//2
    #print(mid, lt, rt)
    if count(mid) <= m : #문제의 조건
        res = mid
        rt = mid-1
    else :
        lt = mid+1

print(res)
