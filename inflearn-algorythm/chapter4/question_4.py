# 마구간 정하기(결정알고리즘)

n, horse_num = map(int, input().split())
magu_num = list()
largest = 0
smallest = float('inf')
for i in range(n) :

    tmp = int(input())
    magu_num.append(tmp)
    largest = max(largest, tmp)
    smallest = min(smallest, tmp)

magu_num.sort()

def arrange_horse(distance) :
    first = magu_num[0]
    cnt = 1
    for i in range(1, len(magu_num)) :
        if magu_num[i]-first >= distance :
            cnt += 1
            first = magu_num[i]
    return cnt

lt = smallest
rt = largest
while lt<=rt :
    mid = (lt+rt)//2
    if arrange_horse(mid) >= horse_num :
        lt = mid+1
        res = mid
    else:
        rt = mid-1

print(res)

# 강사님 풀이

n, c = map(int, input().split())
Line = list()

def Count(len) :
    cnt = 1
    ep = Line[0]
    for i in range(1,n) :
        if Line[i]-ep >= len :
            cnt += 1
            ep = Line[i]
    return cnt

for _ in range(n) :
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1
rt = Line[n-1]
while lt<=rt :
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)