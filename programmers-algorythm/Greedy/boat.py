# 구명보트


def solution(people, limit):
    answer = 0
    # 정렬을 한다. 맨 앞, 맨 뒤 값을 비교할 것이기 때문
    people.sort()
    # 맨 앞 인덱스이다
    st_cursor = 0
    # 맨 뒤 인덱스이다
    end_cursor = len(people) - 1

    # 왼쪽 인덱스가 오른쪽 인덱스보다 커지는 순간 반복문이 종료된다
    while st_cursor <= end_cursor :
        # 만약 왼쪽 값과 오른쪽 값의 합이 최대무게보다 적다면
        # 왼쪽, 오른쪽 인덱스를 하나씩 조정해준다
        if people[st_cursor] + people[end_cursor] <= limit :
            st_cursor += 1
            end_cursor -= 1
        # 만약 왼쪽 값과 오른쪽 값의 합이 최대무게보다 크다면
        # 더 큰 값인 오른쪽 인덱스만 하나 조정한다
        else :
            end_cursor -= 1
        # 인덱스를 조정 후 보트의 수(answer)를 1 증가시킨다
        answer += 1

    return answer

people = [70, 50, 80, 40, 50, 60,40,30,70]
limit = 100

print(solution(people, limit))




