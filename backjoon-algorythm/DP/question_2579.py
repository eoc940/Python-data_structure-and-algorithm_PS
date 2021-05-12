# 2579 계단 오르기

import sys

n = int(sys.stdin.readline())
step = []
for _ in range(n) :
    score = int(sys.stdin.readline())
    step.append(score)
step.insert(0,0)
dy = [0]*(n+1)
dy[0] = 0
dy[1] = step[1]
if n>=2 :
    dy[2] = step[1]+step[2]
    if n>=3 :
        for i in range(3,n+1) :
            first_opt = dy[i-2] + step[i]
            second_opt = dy[i-3] + step[i-1] + step[i]
            dy[i] = max(first_opt, second_opt)

print(dy[n])





