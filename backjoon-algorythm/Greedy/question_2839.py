# 설탕 배달

import sys

n = int(sys.stdin.readline())
answer = 0

three_count = 0
while True :
    num = n - 3*three_count
    if num < 0 :
        answer = -1
        break
    if str(num)[-1] in ['0','5'] :
        answer += num//5 + three_count
        break
    else :
        three_count += 1

print(answer)





