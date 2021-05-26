# 프린터
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()

    # enumerate로 대기목록의 문서에 index를 붙여준다. i는 index, v는 우선순위
    for i, v in enumerate(priorities) :
        queue.append((i,v))

    # 대기목록이 비어 있지 않다면 계속 반복문을 돌린다
    while queue :
        # 1번 인덱스에 우선순위가 들어있으므로 그것만 추출한 리스트를 value에 담는다
        values = [x[1] for x in queue]
        # 만약 맨 앞 값의 우선순위가 최대값과 같다면 popleft를 하고 인쇄 횟수를 1 증가시킨다
        if queue[0][1] == max(values) :
            printed = queue.popleft()
            answer += 1
            # index와 우리가 원하는 location과 일치한다면 인쇄 횟수를 리턴한다
            if printed[0] == location :
                return answer
        # 맨 앞 값과 우선순위가 같지 않다면 popleft를 하고 맨 뒤에 append한다.
        else :
            push_back = queue.popleft()
            queue.append(push_back)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))

