# 한 줄로 서기

import sys

n = int(sys.stdin.readline())
left_count = list(map(int, sys.stdin.readline().split()))

answer = [100 for _ in range(n)]


for i, left in enumerate(left_count):
    # i+1 -> 실제 키
    cnt = 0
    for j,h in enumerate(answer):
        if cnt == left and answer[j] == 100:
            answer[j] = i+1
            break
        if i+1 < h:
            cnt += 1
    # print(answer)

for num in answer:
    print(num, end=" ")