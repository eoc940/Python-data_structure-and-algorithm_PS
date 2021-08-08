### 그리디 알고리즘

- 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미한다
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다
- 그리디 해법은 그 정당성 분석이 중요하다. 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토한다
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많다
- 하지만 코딩 테스트에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론할 수 있어야 풀리도록 출제된다

```
# n이 1이 될 때까지의 연산 횟수 구하기
# n에서 1을 빼거나 k로 나누어질 경우 k로 나눌 수 있음

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

# 다른 방법
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cnt = 0
while True :
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    cnt += (n-target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    cnt += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
cnt += n-1
print(cnt)
```
```
# 곱하기 혹은 더하기(최대값 구하기)
import sys

num = sys.stdin.readline().rstrip()
answer = int(num[0])

for i in range(1, len(num)):
    if answer <= 1 or int(num[i]) <= 1 :
        answer += int(num[i])
    else :
        answer *= int(num[i])

print(answer)
```