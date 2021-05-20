# 순위 검색

from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in range(len(info)) :
        tmp = info[i].split(" ")
        tmp_str, tmp_score = tmp[:-1], tmp[-1]

        for k in range(5) :
            for combi in combinations(tmp_str, k) :
                info_dict[''.join(combi)].append(int(tmp_score))
    #print(info_dict)

    # dict 반복문 돌릴때 .keys안 써도 key로 iterate된다
    for keys in info_dict :
        info_dict[keys].sort()
    print(info_dict)

    for q in query :
        # and와 -를 제외시킴
        tmp_q = q.replace(" and ", "").replace("-","")
        tmp_q_str, tmp_q_score = tmp_q.split(" ")

        tmp_q_score = int(tmp_q_score)

        if tmp_q_str in info_dict :
            scores = info_dict[tmp_q_str]

            # 해당하는 키가 있다면, 즉 점수들이 들어있다면
            if scores :
                #print(scores, tmp_q_score)
                start, end = 0, len(scores)
                while start < end :
                    mid = (start+end)//2
                    if scores[mid] >= tmp_q_score:
                        end = mid
                    else :
                        start = mid + 1
                answer.append(len(scores) - start)

        else :
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))