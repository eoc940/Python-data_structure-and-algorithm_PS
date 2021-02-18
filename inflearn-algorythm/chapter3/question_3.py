# 카드 역배치

def change_card(a,b,num_list) :
    num_list = list(num_list)
    for i in range(a-1, int((a+b)/2)) :
        tmp = num_list[i]
        num_list[i] = num_list[a+b-i-2]
        num_list[a+b-i-2] = tmp
    return num_list

li = [x for x in range(1,21)]
for i in range(10) :
    a,b = map(int, input().split())
    li = change_card(a,b,li)
for i in li :
    print(i, end=" ")

# 강사님 풀이

# 파이썬 swap은 a,b=b,a 하면됨. tmp 이런거 할필요 없음

a=list(range(21))
for _ in range(10) : # 반복문에서 _ 쓰면 변수없이 반복된다
    s, e = map(int, input().split())
    for i in range((e-s+1)//2) :
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0) # 0번 인덱스를 pop하기
for x in a :
    print(x, end=" ")