# 격자판 최대합
'''
n = int(input())
a = list()
for i in range(n) :
    sub_list = list(map(int, input().split()))
    a.append(sub_list)

maximum = 0
for i in range(n) :
    tmp = sum(a[i])
    if tmp > maximum :
        maximum = tmp


for i in range(n):
    tmp = 0
    for j in range(n) :
        tmp += a[j][i]
    if tmp > maximum :
        maximum = tmp

tmp = 0
for i in range(n):
    tmp += a[i][i]
if tmp > maximum :
    maximum = tmp
tmp = 0
for i in range(n) :
    tmp = 0
    tmp += a[i][n-1-i]
if tmp > maximum :
    maximum = tmp

print(maximum)
'''
# 강사님 풀이

n = int(input())
# 이렇게 하면 한번에 이중 리스트 생성
a = [list(map(int, input().split())) for _ in range(n)]

largest = float('-inf')
for i in range(n) :
    sum1 = sum2 = 0
    for j in range(n) :
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2

sum1 = sum2 = 0
for i in range(n) :
    sum1 += a[i][i]
    sum2 += a[i][-i-1] # 혹은 a[i][n-1-i]
    if sum1 > largest :
        largest = sum1
    if sum2 > largest :
        largest = sum2
print(largest)




