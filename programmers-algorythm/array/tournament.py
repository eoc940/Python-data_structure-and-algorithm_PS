# 토너먼트
# math.ceil을 하나 -= p1//2 연산을 하나 시간에서 큰 차이가 없음
# 오히러 math.ceil이 조금 빨랐음
import sys
import math

def is_match(a, b):
    if a+1 == b and a%2 == 1:
        return True
    return False

players, p1, p2 = map(int, sys.stdin.readline().split())

count = 0

while p1 != p2:

    p1 = math.ceil(p1/2)
    p2 = math.ceil(p2/2)
    count += 1

print(count)
