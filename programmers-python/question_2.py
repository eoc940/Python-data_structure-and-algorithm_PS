# n진법으로 표기된 string을 10진법 숫자로 변환하기

def convert_ten(a,b) :
    total = 0
    multiple = 1
    while True :
        total += a%10 * multiple
        multiple *= b
        a = a//10
        if a == 0 :
            break
    return total

num, base = map(int, input().split())
print(convert_ten(num, base))

# 강사님 풀이

num = '3212'
base = 5
answer = int(num, base=base)
print(answer)

'''
int(x, base = 10)함수는 진법 변환을 지원
x를 base진법으로 바꾼다는 의미
단 x는 string형이어야 함
'''