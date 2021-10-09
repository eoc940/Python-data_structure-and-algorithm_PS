# 징검다리

def count(rocks, mid):
    rocks.sort()
    location = 0
    cnt = 0
    for rock in rocks:
        if rock - location >= mid:
            cnt += 1
            location = rock

    return cnt

def solution(distance, rocks, n):
    answer = 0
    lt = 0
    rt = max(rocks)
    while lt <= rt:
        mid = (lt+rt)//2

        if count(rocks, mid) >= len(rocks) - n:
            lt = mid + 1
            answer = mid

        else:
            rt = mid - 1


    return answer

distance = 25
rocks = [2,14,11,21,17]
n = 2
print(solution(distance, rocks, n))
