# 증가수열 만들기(그리디)
from collections import deque

n = int(input())
a = list(map(int, input().split()))
cnt = 0
side = ""
small = 0
a = deque(a)
while a :
    if a[0] < a[-1] and a[0] > small :
        small = a[0]
        side += "L"
        cnt += 1
        a.popleft()
    elif a[0] < a[-1] and a[0] < small :
        if a[-1] > small :
            small = a[-1]
            side += "R"
            cnt += 1
            a.pop()
        else:
            break
    elif a[0] > a[-1] and a[-1] > small :
        small = a[-1]
        side += "R"
        cnt += 1
        a.pop()
    else:
        if a[0] > small :
            small = a[0]
            side += "L"
            cnt += 1
            a.popleft()
        else:
            break
print(cnt)
print(side)

# 강사님 풀이

n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
res = ""
tmp = []

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R',))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)


