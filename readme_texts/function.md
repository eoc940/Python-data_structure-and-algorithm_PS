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