# 대표값
'''
def get_average(scores) :
    scores = list(scores)
    total = 0
    for i in scores :
        total += i
    avg = round(float(total / len(scores)))
    return avg

# 점수가 같다면 앞 학생이 되어야 하므로 부등호에 등호를 붙이지 않음
def get_minimal_index(original_li, li) :
    original_li = list(original_li)
    li = list(li)
    arr_min = li[0]
    select = dict()
    for i in li :
        if i < arr_min :
            arr_min = i

    for j in range(len(li)) :
        if li[j] == arr_min :
            if original_li[j] < 0 :
                select[j] = -1
            else:
                select[j] = 1

    for key, value in select.items() :
        if value == 1 :
            return key

n = int(input())
score_list = list(map(int, input().split()))

subtract_list = list()
make_plus_list = list()

for i in score_list :
    subtract = i - get_average(score_list)
    subtract_list.append(subtract)

for j in range(len(subtract_list)) :
    if subtract_list[j] < 0 :
        make_plus_list.append(-1 * subtract_list[j])
    else:
        make_plus_list.append(subtract_list[j])

index = get_minimal_index(subtract_list, make_plus_list)
print(get_average(score_list), index+1)
'''
# 강사님 풀이

n = int(input())
a = list(map(int, input().split()))

ave=round(sum(a)/n) # a 리스트에 있는 모든 값을 합해줌

# enumerate 쓰는 거 익숙해지기!
min = float("inf")
for idx, x in enumerate(a) :
    tmp=abs(x-ave) # abs 는 절대값 구해줌
    if tmp < min :
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min :  # if-elif 코드에서 73 75 75 이렇게 들어왔다 가정하고 계산해보기
        if x > score :
            score = x
            res = idx+1
print(ave,res)

'''
대표값 오류 수정
round는 round_half_even 방식을 택한다.
a=4.500
print(round(a)) -> 4가 나옴
b=5.500
print(round(b)) -> 6이 나옴
즉 정확히 .500 은 정확히 절반이기 때문에 4와 5중 짝수인 4로 리턴한다.

이걸 막는 방법은
a=67.5
a=a+0.5
a=int(a)
즉 0.5를 더한 후 int 형변환하면 round_half_even 문제에 빠지지 않고
반올림 할 수도 있다.
'''