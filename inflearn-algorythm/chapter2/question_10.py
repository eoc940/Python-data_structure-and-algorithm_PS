# 점수 계산

def get_score(li) :
    li = list(li)
    score_li = [0]*len(li)
    if li[0] == 1 :
        score_li[0] = 1
    else:
        score_li[0] = 0

    for i in range(1,len(li)) :
        if li[i] == 1 :
            score_li[i] = li[i] + score_li[i-1]
        else:
            score_li[i] = 0
    return sum(score_li)

n = int(input())
ox_list = list(map(int, input().split()))

print(get_score(ox_list))

# 강사님 풀이

n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a :
    if x==1 :
        cnt += 1
        sum += cnt
    else :
        cnt = 0

print(sum)