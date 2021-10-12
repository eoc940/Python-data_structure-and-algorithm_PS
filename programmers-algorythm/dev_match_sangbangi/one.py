# 로또의 최고 순위와 최저 순위

def lank(cnt):
    if cnt == 6: return 1
    if cnt == 5: return 2
    if cnt == 4: return 3
    if cnt == 3: return 4
    if cnt == 2: return 5
    return 6

def solution(lottos, win_nums):
    answer = []

    zero_cnt = lottos.count(0)
    right_cnt = 0
    for lotto_num in lottos:
        if lotto_num in win_nums:
            right_cnt += 1

    _max = right_cnt + zero_cnt
    _min = right_cnt
    answer.append(lank(_max))
    answer.append(lank(_min))

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
