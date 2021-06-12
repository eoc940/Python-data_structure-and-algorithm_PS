# 징검다리

def solution(distance, rocks, n):
    answer = 0

    def count(mid) :
        location = 0
        rocks.sort()
        cnt = 0
        for x in rocks :
            if x-location >= mid :
                location = x
                cnt += 1
        return cnt

    lt = 0
    rt = distance

    while lt<=rt :
        mid = (lt+rt)//2
        if count(mid) >= len(rocks) - n :
            lt = mid + 1
            answer = mid
        else :
            rt = mid - 1

    return answer

distance = 25
rocks =	[2, 14, 11, 21, 17]
n = 2
print(solution(distance,rocks, n))