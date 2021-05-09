# 큰 수 만들기

def solution(number, k):
    answer = ''
    while True :
        maxi = "-1"
        for i in range(k+1) : # max를 쓰지 않고 9가 나오면 바로 break를 해도 상관없으므로 이렇게 하는 것이 시간복잡도를 줄일 수 있다.
            if number[i]=="9" :
                maxi = "9"
                break
            elif maxi < number[i] :
                maxi = number[i]
        answer += maxi
        k -= number.find(maxi)
        number = number[number.find(maxi)+1:]

        if k==len(number) :
            break

        if k==0 :
            answer += number
            break

    return answer

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("98382",3))