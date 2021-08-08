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