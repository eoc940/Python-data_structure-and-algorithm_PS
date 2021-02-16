# 정다면체

n, m = map(int, input().split())
n_li = [int(x) for x in range(1, n+1)]
m_li = [int(y) for y in range(1, m+1)]

sum_li = list()
count = dict()
for i in n_li :
    for j in m_li :
        sum_li.append(i+j)

sum_li.sort()

for k in sum_li :
    try : count[k] += 1
    except : count[k] = 1

max_num = max(count.values())

for key, value in count.items() :
    if value == max_num :
        print(key, end=" ")

# 강사님 풀이
# 내 풀이는 매칭을 위해 딕셔너리 사용했지만 key가 연속적인 경우에는
# 굳이 딕셔너리를 사용하지 말고 리스트 인덱스와 value로 매칭 가능

n, m = map(int, input().split())
cnt = [0]*(n+m+3) # 그냥 넉넉하게 잡은것임 n+m 만 해도 다 커버가능, 0으로 다 초기화함
max = 0
for i in range(1, n+1) :
    for j in range(1, j+1) :
        cnt[i+j] += 1

# 최댓값 구하기
for i in range(n+m+1) :
    if cnt[i] > max :
        max = cnt[i]

for i in range(n+m+1) :
    if cnt[i] == max :
        print(i, end=" ")


