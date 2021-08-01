# 곱하기 혹은 더하기

import sys

num = sys.stdin.readline().rstrip()
answer = int(num[0])

for i in range(1, len(num)):
    if answer <= 1 or int(num[i]) <= 1 :
        answer += int(num[i])
    else :
        answer *= int(num[i])

print(answer)




