# 2개 이하로 다른 비트

def find(num):
    if num%2 == 0:
        return num+1
    standard = "0" + bin(num)[2:]
    standard_li = list(standard)
    for i in range(-1, -len(standard_li)-1, -1):
        if standard_li[i] == "0":
            standard_li[i] = "1"
            standard_li[i+1] = "0"
            break
    result = '0b' + ''.join(standard_li)
    return int(result,2)

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(find(num))

    return answer

numbers = [2,7]
print(solution(numbers))

