# 징검다리

def solution(distance, rocks, n):
    answer = 0

    # 징검다리를 건너는 최소 거리를 매개변수로 할 때
    # 징검다리 몇 개를 밟는지를 세 주는 함수
    def count(mid) :
        location = 0
        rocks.sort()
        cnt = 0
        # 최소거리(mid) 이상 되는 거리의 바위를 밟고
        # 그 위치를 현재 위치로 하고 반복함
        for x in rocks :
            if x-location >= mid :
                location = x
                cnt += 1
        return cnt

    lt = 0
    rt = distance
    # 이분탐색을 실행하여 거리의 최소값을 구하고
    # 최소값을 answer에 넣어준다
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