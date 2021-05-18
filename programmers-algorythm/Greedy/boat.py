# 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    st_cursor = 0
    end_cursor = len(people) - 1
    while st_cursor <= end_cursor :
        if people[st_cursor] + people[end_cursor] <= limit :
            st_cursor += 1
            end_cursor -= 1
        else :
            end_cursor -= 1
        answer += 1

    return answer

people = [70, 50, 80, 40, 50, 60,40,30,70]
limit = 100

print(solution(people, limit))




