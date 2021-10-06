# 기능 개발

import math

def solution(progresses, speeds):
    answer = []
    date = []
    for progress, speed in zip(progresses, speeds):
        left_work = 100 - progress
        date.append(math.ceil(left_work / speed))

    print(date)
    finish = date[0]
    load = 0
    for d in date:
        if d <= finish:
            load += 1
        else:
            answer.append(load)
            load = 1
            finish = d

    if load > 0:
        answer.append(load)

    return answer

progresses = [93,30,55]
speeds = [1,30,5]

print(solution(progresses, speeds))