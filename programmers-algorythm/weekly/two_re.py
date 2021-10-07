def solution(scores):
    answer = ''
    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])

        if tmp[i] == max(tmp) and tmp.count(tmp[i]) == 1:
            del tmp[i]
        elif tmp[i] == min(tmp) and tmp.count(tmp[i]) == 1:
            del tmp[i]

        avg = sum(tmp) / len(tmp)
        if avg >= 90:
            answer += "A"
        elif avg >= 80:
            answer += "B"
        elif avg >= 70:
            answer += "C"
        elif avg >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer