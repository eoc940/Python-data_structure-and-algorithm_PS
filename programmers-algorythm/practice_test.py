# 모의고사

def solution(answers):
    winner = []
    first_stu = [1,2,3,4,5]
    second_stu = [2,1,2,3,2,4,2,5]
    third_stu = [3,3,1,1,2,2,4,4,5,5]
    first_score = 0
    second_score = 0
    third_score = 0

    for i in range(len(answers)) :
        if answers[i]==first_stu[i%len(first_stu)] :
            first_score += 1
        if answers[i]==second_stu[i%len(second_stu)] :
            second_score += 1
        if answers[i]==third_stu[i%len(third_stu)] :
            third_score += 1

    maximum = max(first_score, second_score, third_score)
    score_list = [first_score, second_score, third_score]

    for j in range(len(score_list)) :
        if maximum==score_list[j] :
            winner.append(j+1)

    return winner

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))