# 다음 큰 숫자

def binary(n):
    string = ""
    while n > 0:
        string += str(n%2)
        n //= 2
    return string.count("1")

def solution(n):
    cnt_one = binary(n)
    while True:
        n += 1
        if binary(n) == cnt_one:
            return n


print(solution(15))