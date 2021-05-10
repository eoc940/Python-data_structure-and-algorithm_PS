# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    zero_cnt = 0
    cnt = 0
    for x in lottos :
        if x in win_nums :
            cnt += 1
        if x==0 :
            zero_cnt += 1
    maxi = 0
    mini = 0
    for i in range(6,-1,-1) :
        if zero_cnt+cnt == i :
            maxi = 7-i
            if maxi == 7 :
                maxi = 6
        if cnt == i :
            mini = 7-i
            if mini == 7 :
                mini = 6
    answer.append(maxi)
    answer.append(mini)
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))