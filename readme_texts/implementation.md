### 구현
- 구현이란 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다
- 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭한다
- 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
- 실수 연산을 다루고 특정 소수점 자리까지 출력해야 하는 문제
- 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
- 적절한 라이브러리를 찾아서 사용해야 하는 문제

```
# 상하좌우 문제
import sys

n = int(sys.stdin.readline())
direction_list = list(sys.stdin.readline().split())
x, y = 1, 1

go = {"R":(0,1), "U":(-1,0), "L":(0,-1), "D":(1,0)}
for direction in direction_list:
    dx, dy = go[direction]
    if 1 <= x + dx <= n and 1 <= y + dy <= n :
        x += dx
        y += dy

print(x, y)
```
```
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
```
```
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
```
```
# 문자열 재정렬

import sys
string = list(sys.stdin.readline().rstrip())
alpha_list = []
number = 0
answer = ''
for word in string:
    if word.isalpha(): alpha_list.append(word)
    elif word.isdigit(): number += int(word)

alpha_list.sort()
answer = ''.join(alpha_list) + str(number)
print(answer)
```