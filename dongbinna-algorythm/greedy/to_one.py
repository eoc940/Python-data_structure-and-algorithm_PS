# 1이 될 때까지

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cnt = 0
while True :
    if n%k != 0 : n -= 1
    else : n /= k
    cnt += 1
    if n == 1: break
print(cnt)
