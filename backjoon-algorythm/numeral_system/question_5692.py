# 팩토리얼 진법

import sys

def factorial(n) :
    if n==1 :
        return 1
    else :
        return n*factorial(n-1)

while(True) :
    num = int(sys.stdin.readline())
    if num==0:
        break
    cnt = 1
    result = 0
    while(num!=0) :
        last = num%10
        num = num//10
        result += last * factorial(cnt)
        cnt += 1
    print(result)



