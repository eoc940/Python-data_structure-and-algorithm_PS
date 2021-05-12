# N으로 표현

def solution(N, number):
    answer = 0
    dy = []
    recur = 1
    while True :
        tmp = set()
        tmp.add(int(str(N) * recur))
        for i in range(len(dy)) :
            for j in dy[i] :
                for k in dy[len(dy)-i-1] :
                    tmp.add(j+k)
                    tmp.add(j-k)
                    tmp.add(j*k)
                    if k!=0 :
                        tmp.add(j//k)
        recur += 1
        dy.append(list(tmp))
        if len(dy)==9:
            answer = -1
            break
        if number in dy[-1] :
            answer = len(dy)
            break

    return answer

print(solution(5,12))



