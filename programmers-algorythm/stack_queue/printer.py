# 프린터
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i, v in enumerate(priorities) :
        queue.append((i,v))
    while queue :
        values = [x[1] for x in queue]
        if queue[0][1] == max(values) :
            printed = queue.popleft()
            answer += 1
            if printed[0] == location :
                return answer
        else :
            push_back = queue.popleft()
            queue.append(push_back)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))

