# 가장 큰 수

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # 각 숫자는 1000이하이므로 한 자리 숫자일때 세자리 숫자로 바꾼 뒤 sort
    numbers.sort(reverse=True, key=lambda x : x*3)
    #print(numbers)

    return str(int(''.join(numbers)))

#numbers = [3, 30, 34, 5, 9]
numbers = [0,0,0]
print(solution(numbers))
