# 입실 퇴실

from collections import deque


def solution(enter, leave):
    answer = []
    leng = len(enter)
    enter = deque(enter)
    leave = deque(leave)
    while len(enter) != 0 or len(leave) != 0:
        if leave[0] in answer:
            answer.append(leave.popleft())
        else:
            answer.append(enter.popleft())
    result = [0]*leng
    mapping = set()
    print(answer)
    for num in range(1, leng+1):
        loca = list(filter(lambda x : answer[x]==num, range(len(answer))))
        num_list = list(set(answer[loca[0]+1:loca[1]]))
        for n in num_list:
            mapping.add((min(n, num), max(n, num)))
    # print(mapping)
    for n1, n2 in mapping:
        result[n1-1] += 1
        result[n2-1] += 1
    return result

enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution(enter,leave))

