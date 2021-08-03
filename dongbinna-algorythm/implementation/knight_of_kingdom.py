# 왕실의 나이트

import sys

location = list(sys.stdin.readline().rstrip())
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]
alpha_mapping = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
location[0] = alpha_mapping[location[0]]
location[1] = int(location[1])
answer = 0

for i in range(8):
    x = location[0] + dx[i]
    y = location[1] + dy[i]
    if 1<=x<=8 and 1<=y<=8 : answer += 1

print(answer)


