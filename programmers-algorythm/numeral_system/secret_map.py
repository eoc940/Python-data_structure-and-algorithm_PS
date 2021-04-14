# [1차] 비밀지도

def binary(num, n) :
    result = ""
    while num != 0 :
        result = str(num%2) + result
        num = num//2
    digit = n - len(result)
    if digit != 0 :
        for i in range(digit) :
            result = '0' + result
    return result

def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        code1 = binary(arr1[i],n)
        code2 = binary(arr2[i],n)
        tmp = ""
        for j in range(n) :
            if int(code1[j]) or int(code2[j]) :
                tmp += "#"
            else :
                tmp += " "
        answer.append(tmp)
    return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5
print(solution(n, arr1, arr2))

arr3 = [46, 33, 33 ,22, 31, 50]
arr4 = [27 ,56, 19, 14, 14, 10]
m = 6
print(solution(m, arr3, arr4))

