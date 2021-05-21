# 곳감(모래시계)

import sys

n = int(sys.stdin.readline())
yard = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = int(sys.stdin.readline())
move = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for x in move :
    #print(x)
    if x[1] == 0 : # 왼쪽으로 이동
        tmp = yard[x[0]-1][x[2]%n:] + yard[x[0]-1][:x[2]%n]

    else : # 오른쪽으로 이동
        tmp = yard[x[0]-1][n-x[2]%n:] + yard[x[0]-1][:n-x[2]%n]
    #print(tmp)
    yard[x[0]-1] = tmp

total = 0
cursor = 0
for i in range(n//2) :
    total += sum(yard[i][cursor:n-cursor])
    cursor += 1
for i in range(n//2, n) :
    total += sum(yard[i][cursor:n - cursor])
    cursor -= 1
print(total)







