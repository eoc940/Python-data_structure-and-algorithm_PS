# 가장 큰 수
'''
num, m = map(int, input().split())
num = list(map(int, str(num))) # 이 방법 알아두기!!
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]
res = "".join(map(str, stack)) # for 안쓰고 join으로 출력 방법
print(res)
'''


# 다시 풀기
num, m = map(int,input().split())
num = list(map(int, str(num)))
stack = []
for x in num :
    while stack and m>0 and stack[-1]<x :
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0 :
    stack = stack[:-m]

res = "".join(map(str,stack))
print(res)















