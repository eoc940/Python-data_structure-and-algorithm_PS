# k번째 큰 수
n, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
sum_list = list()

for i in range(len(num_list)) :
    for j in range(i+1, len(num_list)) :
        for n in range(j+1, len(num_list)) :
            sum = num_list[i] + num_list[j] + num_list[n]
            sum_list.append(sum)

sum_list = set(sum_list) # 중복 제거하기 위한 방법
sum_list = list(sum_list)
sum_list.sort(reverse=True)

print(sum_list[k-1])

# 강사님 풀이

n, k = map(int, input().split())
a = list(map(int, input().split()))
res=set()
for i in range(n) :
    for j in range(i+1, n) :
        for m in range(j+1, n) :
            # set 자료구조는 append 대신 add
            res.add(a[i] + a[j] + a[m])

res = list(res) # set은 sort 기능이 없어 list로 변환
res.sort(reverse=True)
print(res[k-1])


