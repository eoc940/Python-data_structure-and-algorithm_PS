# 징검다리 건너기

import copy

def success(stone, k, people) :

    for i in range(len(stone)):
        stone[i] -= people
    cnt = 0
    for i in range(len(stone)):
        if stone[i] <= 0:
            cnt += 1
        else :
            cnt = 0
        if cnt >= k:
            return False
    return True

def solution(stones, k):

    answer = 0
    lt = 0
    rt = 200000000
    while lt <= rt:
        mid = (lt+rt)//2
        stones_copy = copy.deepcopy(stones)
        if success(stones_copy, k, mid) :
            lt = mid + 1
            answer = mid
        else:
            rt = mid - 1
    # 통과되는 mid 값에서 1명이 마지막으로 더 건널 수 있기 때문에 1을 더해줌
    return answer + 1

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
#stones = [4,4,4,4,4]
k = 3
print(solution(stones,k))