# 후보키
from itertools import combinations

def validate(relation, indexes):
    values = set()
    for rel in relation:
        tmp = []
        for idx in indexes:
            tmp.append(rel[idx])
        values.add(tuple(tmp))

    if len(values) < len(relation):
        return ()
    else:
        return indexes


def solution(relation):
    answer = []

    idx_list = [x for x in range(len(relation[0]))]
    combin = []
    for i in range(1, len(relation[0])+1):
        combination = combinations(idx_list, i)
        for com in combination:
            combin.append(com)
    for indexes in combin:
        answer.append(validate(relation, indexes))

    result = [ans for ans in answer if ans != ()]
    # print(result)
    answers = []
    for res in result:
        for ans in answers:
            if set(res) & set(ans) == set(ans):
                break
        else:
            answers.append(res)

    # print(answers)
    return len(answers)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))



