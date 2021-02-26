# 랜선자르기(결정알고리즘)
'''
n, k = map(int, input().split())
a = list()
for i in range(n) :
    a.append(int(input()))

a.sort()

lt = 0
rt = n-1
first_index = 0
second_index = 0
while lt<=rt :
    mid = (lt+rt)//2
    cnt = 0
    for i in range(n) :
        cnt += a[i]//a[mid]
    if cnt < k :
        rt = mid - 1
        first_index = mid
    elif cnt > k :
        lt = mid + 1
        second_index = mid

left_index = min(first_index, second_index)
right_index = max(first_index, second_index)
if right_index==left_index :
    for i in range(a[right_index],0,-1) :
        total = 0
        for j in a:
            total += (j // i)
        if total >= k:
            print(i)
            break
else:
    for i in range(a[right_index], a[left_index], -1):
        total = 0
        for j in a:
            total += j // i
        if total >= k:
            print(i)
            break
'''
# 강사님 풀이
# 이분탐색 사용할 경우 - 어느 범위 안에 있다는 걸 알 수 있을 때 사용
n, k = map(int, input().split())
a = list()
largest = 0
for i in range(n) :
    tmp = int(input())
    a.append(tmp)
    largest=max(largest,tmp)

lt = 1
rt = largest

def get_count(a, mid) :
    a = list(a)
    cnt = 0
    for i in a :
        cnt += i//mid
    return cnt

res = 0
while lt<=rt :
    mid = (lt+rt)//2
    if get_count(a,mid) < k:
        rt = mid-1
    elif get_count(a,mid) >= k :
        lt = mid+1
        res = mid

print(res)




