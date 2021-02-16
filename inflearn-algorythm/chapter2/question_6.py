# 자릿수의 합

def digit_sum(x) :
    sum = 0
    while x>0 :
        sum += x%10
        x = int(x/10)
    return sum

n = int(input())
arr = list(map(int, input().split()))
sum_list = list()

for i in range(len(arr)) :
    sum_list.append(digit_sum(arr[i]))

max_num = max(sum_list)

for i in range(len(arr)) :
    if sum_list[i] == max_num :
        print(arr[i])
        break

# 강사님 풀이

n=int(input())
a=list(map(int, input().split()))

def digit_sum(x) :
    sum = 0
    while x > 0 :
        sum += x%10
        x = x//10 # x를 10으로 나눈 몫
    return sum

def digit_sum_2(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)
    return sum

max = -2147000000
for x in a :
    tot = digit_sum(x)
    if tot>max :
        max = tot
        res = x

print(res)
