# 프린터

from collections import deque

def solution(priorities, location):
    answer = []
    prior_list = sorted(priorities)
    for i, val in enumerate(priorities):
        priorities[i] = (i, val)

    priorities = deque(priorities)

    while priorities:
        idx, prior = priorities.popleft()
        if prior == prior_list[-1]:
            prior_list.pop()
            answer.append(idx)
        else:
            priorities.append((idx,prior))

        if answer and answer[-1]==location:
            return len(answer)


a = [1, 1, 9, 1, 1, 1]
b = 0
print(solution(a,b))




