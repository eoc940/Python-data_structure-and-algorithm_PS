# 카펫

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    abstract_leng = total**(1/2)
    if abstract_leng==int(abstract_leng) :
        possible_garo = int(abstract_leng)
    else :
        possible_garo = int(abstract_leng+1)
    possible_sero = possible_garo

    while True :
        #print(possible_garo, possible_sero)
        #print(total)
        for i in range(possible_sero, 0, -1) :
            if possible_garo*i < total :
                break
            if possible_garo*i==total and (possible_garo-2)*(i-2)==yellow:
                answer.append(possible_garo)
                answer.append(i)
                return answer
        possible_garo += 1


    return answer

print(solution(50,22))
