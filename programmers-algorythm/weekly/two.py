def get_grade(scores):
    answer = ""
    for score in scores:
        if score >= 90: answer += "A"
        elif score >= 80: answer += "B"
        elif score >= 70: answer += "C"
        elif score >= 50: answer += "D"
        else: answer += "F"
    return answer

def solution(scores):
    answer = []
    for i in range(len(scores)):
        tmp = list()
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        if max(tmp) == scores[i][i] and tmp.count(scores[i][i]) == 1:
            tmp.remove(scores[i][i])
        elif min(tmp) == scores[i][i] and tmp.count(scores[i][i]) == 1:
            tmp.remove(scores[i][i])
        average = sum(tmp) / len(tmp)
        answer.append(average)

    return get_grade(answer)

scores = [[70,49,90],[68,50,38],[73,31,100]]
print(solution(scores))