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