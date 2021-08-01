# 공포도

import sys

n = int(sys.stdin.readline())
scary = list(map(int, sys.stdin.readline().split()))

scary.sort(reverse=True)
answer = 0
idx = 0
while idx < len(scary):
    idx += scary[idx]
    answer += 1

print(answer)
