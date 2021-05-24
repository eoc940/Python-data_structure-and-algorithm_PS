# 격자판 회문수

import sys

answer = 0
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]


for i in range(7) :
    for j in range(3) :
        for x in range(2) :
            if nums[i][x+j] != nums[i][4-x+j] :
                break
        else :
            answer += 1
        for k in range(2) :
            if nums[k+j][i] != nums[4-k+j][i] :
                break
        else :
            answer += 1

print(answer)
