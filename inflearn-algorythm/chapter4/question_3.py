# 뮤직비디오(결정알고리즘)
'''
n, k = map(int, input().split())
a = list(map(int,input().split()))

lt = 1
rt = sum(a)

def possible_size(a, k, mid) :
    a = list(a)
    num_dvd = 0
    idx = 0
    while True :
        tmp = 0
        ddx = idx
        for i in range(ddx, len(a)) :
            idx += 1
            if tmp+a[i] <= mid :
                tmp += a[i]
                if i == len(a)-1:
                    num_dvd += 1
                    if num_dvd <= k:
                        return True
                    else:
                        return False
                continue
            else :
                idx -= 1
                num_dvd += 1
                break

res = 0
while lt<=rt :
    mid = (lt+rt)//2
    if possible_size(a, k, mid) :
        rt = mid-1
        res = mid
    else:
        lt = mid+1


print(res)
'''
# 강사님 풀이

def count(capacity) :
    cnt=1
    sum=0
    for x in music : # music을 매개변수 넣을 필요 없음
        if sum+x > capacity :
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
music = list(map(int,input().split()))
maxx = max(music)

lt = 1
rt = sum(music)
res = 0
while lt<=rt :
    mid =(lt+rt)//2
    if mid >= maxx and count(mid) <= m :
        res = mid
        rt = mid-1
    else:
        lt = mid+1
print(res)
