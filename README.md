# Data-structure-and-Algorythm

### 사용 기술, 작업 환경
- python 3.7
- pycharm

#### 백준, 프로그래머스, 인프런 등 자료구조&알고리즘 문제 풀이입니다

## 자료구조 & 알고리즘 정리

####복잡도(Complexity)
- 복잡도는 알고리즘의 성능을 나타내는 척도
- 시간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
- 공간 복잡도 : 특정한 크기의 입력에 대해서 알고리즘의 메모리 사용량 분석
- 동일한 기능을 수행하는 알고리즘이 있다면 일반적으로 복잡도가 낮을수록 좋은 알고리즘

#### 빅오 표기법(Big-O Notation)
- 가장 빠르게 증가하는 항만을 고려하는 표기법
- 함수의 상한만을 나타냄
- 예를 들어 연산 횟수가 3N**3 + 5N**2 + 100000인 경우 차수가 가장 큰 항만 남겨서 O(N**3)으로 표현한다
- O(1) : 상수 시간, O(logN) : 로그 시간, O(N) : 선형 시간, O(NlogN) 로그 선형 시간, O(N**2) : 이차 시간, O(N**3) : 삼차 시간, O(2**n) : 지수 시간 -> 뒤로 갈수록 나쁨

#### 수행 시간 측정
```
import time
start_time = time.time()

# 프로그램 소스코드
end_time = time.time()
print("time : ", end_time - start_time)
```

#### 자료형
- 모든 프로그래밍은 결국 데이터를 다루는 행위다
- 파이썬에서는 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전 등이 있다

1. 정수형
- 정수를 다루는 자료형, 양의 정수, 음의 정수, 0이 포함됨

2. 실수형
- 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리된다
- 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있습니다(5. -> 5.0, -.7 -> -0.7)
- IEEE754 표준에서는 실수형을 저장하기 위해 4바이트, 혹은 8바이트의 고정된 크기의 메모리를 할당하므로 
컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계가 있다
- 10진수 체계에서는 0.3과 0.6을 더한 값이 정확이 0.9로 떨어지지만 2진수에서는 0.9를 정확히 표현할 수 있는 방법이 없다
- 컴퓨터는 최대한 0.9와 가깝게 표현하지만, 미세한 오차가 발생하게 된다
- a = 0.3 + 0.6 ---> 0.89999999999 --> 0.9와 다르다고 나옴
- 이럴 때는 round()함수를 이용하여 해결할 수 있다
- 파이썬에서 나누기 연산자(/)는 나눠진 결과를 실수형으로 반환한다
- 몫 연산자는 (//)이다
- 거듭 제곱 연산자(**), 나머지 연산자(%) 등이 있다



3. 지수형
- 파이썬에서는 e나 E를 이용한 지수 표현 방식을 이용할 수 있다
- e나 E 다음에 오는 수는 10의 지수부를 의미한다
- 예를 들어 1e9라고 입력하게 되면, 10의 9제곱(1,000,000,000)이 된다
- 유효숫자e지수 = 유효숫자X10지수
- 지수 표현 방식은 임의의 큰 수를 표현하기 위해 자주 사용됨
- 최단 경로 알고리즘에서는 도달할 수 없는 노드에 대해 최단 거리를 무한(INF)으로 설정하곤 한다
- 이때 가능한 최대값이 10억 미만이라면 무한(INF)의 값으로 1e9를 이용할 수 있다
- 75.25e1 -> 752.5


4. 리스트 자료형
- 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
- 사용자 입장에서 C나 자바에서의 배열(Array)의 기능 및 연결 리스트와 유사한 기능을 지원한다
- 리스트 대신에 배열 혹은 테이블이라고 부르기도 한다
- 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 []를 이용한다
- 리스트의 원소에 접근할 때는 인덱스로 접근한다
- 인덱스는 음수도 가능한데, -1은 뒤에서 첫번째, -3은 뒤에서 세번째
- 인덱싱과 슬라이싱이 가능하다
- 리스트 컴프리헨션 : 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 가능
- array = [i for i in range(10)] -> [0,1,2,3,4,5,6,7,8,9]
- array = [i for i in range(20) if i%2 == 1] -> [1,3,5,7,9,11,13,15,17,19]
- append() : 리스트에 원소를 하나 삽입. O(1)
- sort() : 기본 정렬 기능. O(NlogN)
- reverse() : 리스트의 원소의 순서를 뒤집는다. O(N)
- insert() : 특정한 인덱스 위치에 원소를 삽입. O(N)
- count() : 리스트에서 특정한 값을 가지는 데이터의 값을 셈. O(N)
- remove() : 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러개면 하나만 제거. O(N)
- 리스트에서 특정 값을 가지는 원소를 모두 제거 : a=[1,2,3,4,5,5], remove_set = {3,5}, result=[i for i in a if i not in remove_set] -> [1,2,4]

5. 문자열 자료형
- 문자열 변수를 초기화할 때는 큰따옴표나 작은따옴표를 이용한다
- 백슬래시(\)를 사용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있다
- data = "Don't you know \"Python\"?"
- 문자열 변수에 덧셈과 곱셈이 가능하다
- 문자열도 인덱스와 슬라이싱을 사용할 수 있지만 특정 인덱스의 값을 변경할 수는 없다 -> 리스트로 변환 후 값을 변경하고 나서 join으로 합친다

6. 튜플 자료형
- 한 번 선언된 값을 변경할 수 없다
- 소괄호를 사용한다
- 리스트에 비해 상대적으로 공간 효율적이다(기능이 제한적이기 때문) -> 메모리 적게 사용
- 서로 다른 성질의 데이터를 묶어서 관리할 때 사용 -> 최단 경로 알고리즘에서 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용
- 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
- 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다
- 리스트보다 메모리를 효율적으로 사용해야 할 때

7. 사전 자료형
- 키와 값의 쌍을 데이터로 가지는 자료형, 값을 순차적으로 저장하지는 않음
- 변경 불가능한 자료형을 키로 사용할 수 있다
- 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다
- 키 존재 여부를 in 키워드로 알 수 있음. data = {"사과":"apple"}, if "사과" in data : print("True") -> True
- 키 데이터만 뽑을 때는 keys(), 값 데이터만 뽑을 때는 values()

8. 집합 자료형
- 중복을 허용하지 않고 순서가 없다
- 리스트 혹은 문자열을 이용해서 초기화할 수 있다 -> set()함수 사용
- 혹은 중괄호 안에 각 원소를 콤마(,)로 구분하여 초기화할 수 있다
- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다
- 원소 하나 추가할 땐 .add(원소), 원소 여러개 추가할 땐 .update([원소1, 원소2...]), 특정한 값 원소 삭제할 땐 .remove(값)


#### 기본 입출력

###### 자주 사용되는 표준 입력 방법
- input() 함수는 한 줄의 문자열을 입력 받는 함수이다
- map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다

```
예시) 공백을 기준으로 구분된 데이터를 입력 받을 때 다음과 같이 사용
list(map(int, input().split()))
예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다
a,b,c = map(int, input().split())
```
- sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용한다
- 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용한다

###### 자주 사용되는 표준 출력 방법
- print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다
- 줄 바꿈을 원치 않는 경우 'end'속성을 이용할 수 있다
- f-string 은 파이썬 3.6부터 사용 가능하며 문자열 앞에 접두사 'f'를 붙여 사용한다
- 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다
```
answer = 7
print(f"정답은 {answer}입니다")
```

###### 조건문의 간소화
- 조건부 표현식은 if~else문을 한 줄에 작성할 수 있도록 해준다. if가 중간에 들어간다
```
score = 85
result = "Success" if score>=80 else "Fail"
```
- 다른 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다
```
x = 15
if 0<x<20 :
    print("x는 0이상 20미만의 수다")
```

###### 반복문

- while 뒤에 조건이 들어감
```
i = 1
result = 0
while i <= 9:
    result += i
    i += 1
print(result) -> 45 
```
- 무한 루프란 끊임없이 반복되는 반복 구문을 의미한다. 반복문을 작성 뒤 탈출 가능한지 확인해야 함
```
i = 10
while i>5 :
    print(i)
```
- for문의 구조는 특정한 변수를 이용하여 in 뒤에 오는 데이터에 포함되어 있는 원소를 첫 번째 인덱스부터 차례로 하나씩 반복된다
```
array = [9,8,7,6,5]
for x in array:
    print(x)
```
- for문에서 연속적인 값을 차례로 순회할 때는 range()를 주로 사용한다
- 이때 range(시작, 끝 + 1) 형태로 사용한다
```
result = 0
for i in range(1,10):
    result += i
print(result) -> 45
```
###### 함수
- 내장 함수 : 파이썬이 기본적으로 제공하는 함수
- 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수
- 매개변수 : 함수 내부에서 사용할 변수, 반환 값 : 함수에서 처리된 결과를 반환
```
def 함수명(매개변수):
    실행할 소스코드
    return 반환 값
```
- 파라미터이 변수를 직접 지정할 수 있다. 매개변수의 순서가 달라도 상관없다
```
def add(a, b):
    print('함수의 결과:', a + b)
    
add(b = 3, a = 7)
```

- global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 된다
```
a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()
    
print(a) -> 10
```

- 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다
```
def operator(a,b):
    plus = a + b
    minus = a - b
    return plus, minus

c, d = operator(7,3)
print(a,b,c,d) -> 7,3,10,4
```
- 람다 표현식 예시
```
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a,b : a+b, list1, list2)
print(list(result)) -> [7,9,11,13,15]
```

###### 실전에서 유용한 표준 라이브러리
- 내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
```
# sum, min, max는 간단하니까 스킵

# eval() -> 문자열 안의 연산을 수행
result = eval("(3+5)*7")
print(result) -> 56

# sorted() with key
array = [('a',3),('b',5),('c',1)]
result = sorted(array, key = lambda x : x[1], reverse=True)
print(result) -> [('b',5),('a',3),('c',1)]
```
- itertools : 반복되는 형태의 데이터를 처리하기 위한 기능 제공. 특히 순열과 조합 라이브러리 주로 사용됨
```
# 순열 : permutations
# 조합 : combinations
# 중복순열 : product
# 중복조합 : combinations_with_replacement

# Counter : 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등작했는지 알려줌
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) -> 3
print(dict(counter)) -> {'red':2, 'blue':3, 'green':1}
```
- heapq : 힙 자료구조를 제공. 일반적으로 우선순위 큐 기능을 구현하기 위해 사용됨
- bisect : 이진 탐색 기능을 제공
- collections : deque, Counter 등의 유용한 자료구조를 포함
- math : 필수적인 수학적 기능 제공. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함
```
# 최대 공약수를 구한 때는 math 라이브러리의 gcd() 함수를 이용할 수 있다
import math

# 최소 공배수(lcm)를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21,14)) # 최대 공약수 계산 -> 7
print(lcm(21,14)) # 최소 공배수 계산 -> 42
```

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

### 그래프 탐색 알고리즘 : DFS/BFS
- 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다
- 대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있다
- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야 한다

##### 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조이다
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다
- 파이썬에서는 리스트 자료구조를 사용하면 된다
- append, pop함수의 시간복잡도는 O(1)이다

##### 큐 자료구조
- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조이다
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화할 수 있다
- 파이썬에서는 deque 자료구조를 사용하는 것이 좋다
- append, popleft함수의 시간복잡도는 O(1)이다

##### 재귀 함수
- 재귀 함수란 자기 자신을 다시 호출하는 함수이다
- 스택 자료구조에 함수에 대한 정보가 차례로 메모리에 담기는 형태이다
- 따라서 무한정으로 재귀 함수가 호출되면 에러가 발생한다
- 재귀 함수를 문제 풀이에서 사용할 때는 종료 조건을 명시해야 한다
- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다
- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 내부의 스택 프레임에 쌓인다 -> 스택 대신 재귀를 이용하는 경우가 많다

##### DFS
- DFS는 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다
- 스택 자료구조 혹은 재귀 함수를 이용하며 동작 과정은 다음과 같다
    - 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다
    - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
    - 더 이상 위의 과정을 수행할 수 없을 때까지 반복한다
    
##### BFS
- BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다
- BFS는 큐 자료구조를 이용하며 동작 과정은 다음과 같다
    - 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
    - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다
    - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다
```
# 음료수 얼려 먹기

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
ices = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    global answer
    dq = deque()
    dq.append((x,y))
    ices[x][y] = 1
    while dq:
        tx, ty = dq.popleft()
        for i in range(4):
            xx = tx + dx[i]
            yy = ty + dy[i]
            if 0<=xx<n and 0<=yy<m and ices[xx][yy] == 0:
                ices[xx][yy] = 1
                dq.append((xx,yy))
    answer += 1

for i in range(n):
    for j in range(m):
        if ices[i][j] == 0: bfs(i,j)

print(answer)
```
```
# 미로 탈출

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

dq = deque()
dq.append((0,0))


while dq:
    for _ in range(len(dq)):
        tx, ty = dq.popleft()
        if tx == n-1 and ty == m-1 :
            answer = maze[tx][ty]
            break
        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]
            if 0<=x<n and 0<=y<m and maze[x][y]==1:
                maze[x][y] = maze[tx][ty] + 1
                dq.append((x,y))
    for x in maze:
        print(x)
    print()

print(answer)
```

### 정렬 알고리즘

- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다

##### 선택 정렬
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다
```
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
```
- 선택 정렬의 시간 복잡도
  - 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다
  - 구현 방식에 따라서 사소한 오차가 있을 수 있지만, 전체 연산 횟수는 다음과 같다
    - N + (N-1) + (N-2) + ... + 2
  - 이는 (N2 + N -2) / 2 로 표현할 수 있는데, 빅오 표기법에 따라 O(N2)이다

##### 삽입 정렬
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 더 효율적으로 작동한다
```
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
```
- 삽입 정렬의 시간 복잡도는 O(N2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다
  - 최선의 경우 O(N)의 시간 복잡도를 가진다
  - 이미 정렬되어 있는 상태에서 다시 삽입 정렬을 수행한다면?
    - 전체 시간 복잡도는 O(N)
  
##### 퀵 정렬
- 기준 데이터를 설정하고 그 가준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나이다
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정한다
- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다
  - 너비 X 높이 = N X logN = NlogN
- 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다
- 하지만 최악의 경우 O(N2)의 시간 복잡도를 가진다
  - 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면 어떻게 될까?
    - 전체 시간 복잡도는 O(N2)
```
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # array의 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗 보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗 보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```
```
파이썬으로 조금 더 쉽게 작성
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

##### 계수 정렬
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘이다
  - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능하다
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N + K)를 보장한다 
```
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```
- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)이다
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다
  - 데이터가 0과 999999로 단 2개만 존재하는 경우를 생각해 보면 된다
- 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있다
  - 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적이다