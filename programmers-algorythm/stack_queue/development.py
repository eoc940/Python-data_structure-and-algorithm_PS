# 기능개발

def solution(progresses, speeds):
    answer = []
    idx = 0
    cnt = 0

    while(sum(progresses)!=0) :
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
            if progresses[i] >= 100 :
                progresses[i] = 0
                speeds[i] = 0

        for j in range(idx, len(progresses)) :
            if progresses[j] == 0 :
                cnt += 1
            else :
                break
        if cnt != 0 :
            answer.append(cnt)
            idx += cnt
        cnt = 0

    return answer

a = [95, 90, 99, 99, 80, 99]
b = [1, 1, 1, 1, 1, 1]
print(solution(a,b))

