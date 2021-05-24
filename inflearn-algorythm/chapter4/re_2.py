# 랜선자르기(결정알고리즘)

import sys

k, n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]
lines.sort()

lt = 0
rt = lines[-1]
res = 0
while lt<=rt :
    mid = (lt+rt)//2
    answer = 0
    for x in lines :
        answer += x//mid
    if answer < n :
        rt = mid-1
    else :
        lt = mid+1
        res = mid # 여기서는 else조건이 문제 조건을 만족하는 조건이므로 이때 res에 넣어줌
print(res)


