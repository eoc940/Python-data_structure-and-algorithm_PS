# 체육복

def solution(n, lost, reserve):

    fil_lost = set(lost) - set(reserve)
    fil_reserve = set(reserve) - set(lost)
    answer = n - len(fil_lost)
    for x in fil_lost :
        if x-1 in fil_reserve :
            fil_reserve.remove(x-1)
            answer += 1
            continue
        elif x+1 in fil_reserve :
            fil_reserve.remove(x+1)
            answer += 1
            continue
    return answer

print(solution(5,[2,3,5],[1,4]))