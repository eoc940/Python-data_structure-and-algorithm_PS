# 실패율

from collections import defaultdict

def solution(N, stages):
    answer = []
    score_mapping = defaultdict(float)
    for i in range(1,N+1):
        devide = 0
        stage_in = 0
        for x in stages:
            if x>=i : devide += 1
            if x==i : stage_in += 1
        if devide == 0: score_mapping[i] = 0
        else: score_mapping[i] = stage_in / devide
    a = sorted(score_mapping.items(), reverse=True, key=lambda x : x[1])
    #print(a)
    for x in a:
        answer.append(x[0])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = [4,1,2,3,2]
print(solution(N, stages))