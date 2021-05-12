# 10872 팩토리얼

import sys

def factorial(num) :
    if num==0 :
        return 1
    return num * factorial(num-1)

n = int(sys.stdin.readline().rstrip())

print(factorial(n))

