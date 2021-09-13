# 이진 변환 반복

def convert(num):
    n = num//2
    if n==0:
        return str(num%2)
    return convert(n)+str(num%2)

def solution(s):
    repeat, remove = 0, 0
    while s != "1":
        repeat += 1
        remove += s.count("0")
        s = s.replace("0", "")
        s = convert(len(s))
    return [repeat, remove]

s = "110010101001"
print(solution(s))
print(convert(6))