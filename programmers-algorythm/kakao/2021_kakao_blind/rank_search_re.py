# 순위 검색

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for idx, info_str in enumerate(info):
        info_li = info_str.split()
        info_str, score = info_li[:-1], int(info_li[-1])
        for i in range(len(info_str)+1):
            for x in combinations(info_str, i):
                info_dict[''.join(x)].append(score)

    for key in info_dict:
        info_dict[key].sort()

    for que in query:
        que = que.replace(" and ", "").replace("-", "").split()
        if len(que) == 1:
            que.insert(0, "")
        #print(que, int(que[1]), info_dict[que[0]])
        location = bisect_left(info_dict[que[0]], int(que[1]))
        answer.append(len(info_dict[que[0]]) - location)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))




