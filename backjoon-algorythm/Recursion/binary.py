# 이진수 변환

import sys

def convert_binary(num) :
    if num>0 :
        convert_binary(num//2)
        print(num % 2, end="")

n = int(sys.stdin.readline())

convert_binary(n)

