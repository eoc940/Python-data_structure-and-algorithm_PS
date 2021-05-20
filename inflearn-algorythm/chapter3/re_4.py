# 두 리스트 합치기

import sys

n = int(sys.stdin.readline())
first = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
second = list(map(int, sys.stdin.readline().split()))
#print(first)
#print(second)

first.extend(second)
first.sort()
for x in first :
    print(x, end=" ")


