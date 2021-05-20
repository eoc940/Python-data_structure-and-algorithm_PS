# 격자판 최대합

import sys

n = int(sys.stdin.readline())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
maxi = 0
for i in range(n) :
    tmp = 0
    for j in range(n):
        tmp += num[i][j]
    if maxi < tmp :
        maxi = tmp

for i in range(n) :
    tmp = 0
    for j in range(n):
        tmp += num[j][i]
    if maxi < tmp :
        maxi = tmp
tmp = 0
for i in range(n) :
    tmp += num[i][i]
if maxi < tmp :
    maxi = tmp

tmp = 0
for i in range(n):
    tmp += num[i][4-i]
if maxi < tmp :
    maxi = tmp
print(maxi)
