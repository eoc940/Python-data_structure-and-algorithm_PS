# 멀쩡한 사각형

import math

def solution(w,h):
    all_square = w*h
    mul = math.gcd(w,h)

    return all_square - (w+h-mul)

w, h = 8,12
print(solution(w,h))
