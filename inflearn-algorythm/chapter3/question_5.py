# 수들의 합
'''
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0
for i in range(n) :
    tmp = 0
    while tmp < m :
        tmp += num_list[i]
        i += 1
        if tmp == m :
            cnt += 1
            break
        elif tmp > m :
            break
        if i >= len(num_list) :
            break

print(cnt)
'''
# 강사님 풀이

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True :
    if tot < m :
        if rt < n :
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m :
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)

