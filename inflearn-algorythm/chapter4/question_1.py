# 이분검색
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1
for i in range(n) :
    mid = (lt + rt) // 2
    if a[mid] > k :
        rt = mid - 1
    elif a[mid] < k :
        lt = mid + 1
    else:
        print(mid+1)
        break
'''
# 강사님 풀이

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1
while lt <= rt :
    mid = (lt+rt)//2
    if a[mid] == k :
        print(mid+1)
        break
    elif a[mid] > k :
        rt = mid-1
    else:
        lt = mid+1
