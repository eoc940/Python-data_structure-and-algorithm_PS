# 가장 큰 수

import sys

n, d = map(int, sys.stdin.readline().split())

stack = []

n = str(n)

for x in n :
    print(''.join(stack), d)
    while stack and d>0 and stack[-1] < x :
        stack.pop()
        d -= 1
    stack.append(x)

# 정해진 숫자만큼 삭제가 되지 않았을 때
if d != 0 :
    stack = stack[:-d]

print(''.join(stack))





