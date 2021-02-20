# 알파벳 출력하기

def print_alphabet(n) :
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if n == 0 :
        print(alpha)
    elif n == 1 :
        print(alpha.upper())

num = int(input())
print_alphabet(num)

# 강사님 풀이

import string
string.ascii_lowercase # 소문자
string.ascii_uppercase # 대문자
string.ascii_letters # 대소문자 연속출력
string.digits # 숫자 0123456789

