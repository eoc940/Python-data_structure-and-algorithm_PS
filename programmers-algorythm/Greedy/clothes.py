# 체육복

def solution(n, lost, reserve):

    # 빌려야 하는 학생 집합
    fil_lost = set(lost) - set(reserve)
    # 빌려줄 수 있는 학생 집합
    fil_reserve = set(reserve) - set(lost)

    # 아직 도난당한 학생들이 체육복을 받지 못했을때의 answer
    answer = n - len(fil_lost)

    # 빌려야 하는 학생들으로 반복문을 돌림
    for x in fil_lost :
        # 앞 학생이 빌려줄수 있다면 앞 학생을 빌려줄 수 있는 set에서 제거 후
        # answer(옷이 있는 학생수)에 1을 더함
        if x-1 in fil_reserve :
            fil_reserve.remove(x-1)
            answer += 1
            # 옷을 빌렸으므로 밑을 수행하지 않고 바로 반복문으로 돌아감
            continue
        # 뒤 학생이 빌려줄수 있다면 뒤 학생을 빌려줄 수 있는 set에서 제거 후
        # answer(옷이 있는 학생수)에 1을 더함
        elif x+1 in fil_reserve :
            fil_reserve.remove(x+1)
            answer += 1
            # 옷을 빌렸으므로 밑을 수행하지 않고 바로 반복문으로 돌아감
            continue

    return answer

print(solution(5,[2,3,5],[1,4]))