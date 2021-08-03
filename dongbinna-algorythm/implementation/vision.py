# 시각

import sys

n = int(sys.stdin.readline())
answer = 0
three_per_hour = 0
for i in range(60):
    for j in range(60):
        if "3" in str(i) or "3" in str(j):
            three_per_hour += 1

for i in range(n+1):
    if "3" in str(i):
        answer += 3600
    else :
        answer += three_per_hour

print(answer)

