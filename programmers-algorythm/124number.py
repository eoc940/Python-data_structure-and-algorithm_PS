# 124 나라의 숫자

def convert(n) :
    k = n-1
    if n==0 :
        return ""
    else :
        return convert(k//3) + str(k%3+1)

def solution(n):
    num = convert(n)
    answer = ''
    for x in num :
        if x=='3' :
            answer += '4'
        else :
            answer += x
    return answer

print(convert(2))
print(solution(9))



