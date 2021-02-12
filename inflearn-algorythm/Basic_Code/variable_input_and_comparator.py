'''
변수이름과 연산자

a=input("숫자를 입력하세요 : ")
print(a)

a,b = input("숫자를 입력하세요 : ").split()
# split은 띄어쓰기 기준으로 분리하여 넣어준다
# input은 string으로 받아주는 것이다
print(a,b)
# 문자열로 인식하기 때문에 10 5를 입력하면 105가 출력된다
print(type(a))
print(a+b)
print(type(a+b))

a,b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(a+b)

# map은 괄호 첫번째의 자료형으로 괄호 뒤의 값을 매핑하는 것
a,b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # a를 b로 나눈 몫
print(a%b) # a를 b로 나눈 나머지
print(a**b) # a의 b승 -> 2**3 = 2의 세제곱 = 8
'''

a=4.3
b=5
c=a+b
print(type(c)) # float와 int의 연산은 float

