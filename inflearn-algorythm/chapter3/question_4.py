# 두 리스트 합치기
'''
def add_list(a,b) :
    total_list = a+b
    total_list.sort()
    return total_list

first_index = int(input())
first_list = list(map(int, input().split()))
second_index = int(input())
second_list = list(map(int, input().split()))
for i in add_list(first_list, second_list) :
    print(i, end=" ")
'''
# 풀이 2
'''
first_idx = int(input())
first_li = list(map(int, input().split()))
second_idx = int(input())
second_li = list(map(int, input().split()))
for i in range(first_idx+second_idx) :
    if first_li[0] >= second_li[0] :
        print(second_li[0], end=" ")
        if len(second_li) > 1 :
            del second_li[0]
        else:
            second_li[0] = float('inf')

    else :
        print(first_li[0], end=" ")
        if len(first_li) > 1 :
            del first_li[0]
        else:
            first_li[0] = float('inf')
'''
# 강사님 풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1=p2=0
c=[]
while p1<n and p2<m :
    if a[p1] <= b[p2] :
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1<n :
    c=c+a[p1:]
if p2<m :
    c=c+b[p2:]

for x in c:
    print(x, end=" ")