# 쇠막대기

import sys

laser = sys.stdin.readline().rstrip()
stack = []
answer = 0

for i in range(len(laser)) :
    if laser[i]=="(" :
        stack.append(1)

    else : # ) 이 들어온 경우
        stack.pop()
        if laser[i-1]=="(" : # 레이저 쏘는 경우
            answer += len(stack)
        else : # 연속해서 ")"가 오는 경우
            answer += 1

print(answer)



