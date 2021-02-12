"""
변수명 정하기
1. 영문과 숫자, _로 이루어진다
2. 대소문자를 구별한다
3. 문자나, _로 시작한다
4. 특수문자를 사용하면 안된다(&, %등)
5. 키워드를 사용하면 안된다(if, for등)
"""

a = 1
A = 2
# 2b = 4 -> 불가능
print(a)
print(A)
print(a, A, sep="...")
print()
a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환(swap)
a, b = 10, 20
a,b = b,a
print(a,b)

#변수 타입
a=12345
print(type(a))
#int형이라고 출력된다

"""
현재 setting - inspection - python과 inspection - proofreading - typo 를 꺼놓았음
코드는 돌아가는데 파이썬 규칙을 어긴 코드에 줄이 뜨는데 그것을 없애기 위한 것
"""

a=12.3345252
print(a)

a='student'
print(a)

#출력 방식
#print는 자동으로 줄바꿈이 됨
print("number")
a,b,c=1,2,3
print(a,b,c)
print("number",a,b,c)
# sep -> separate의 약자로, 출력할 것들 사이에 값을 넣어줌
print(a,b,c, sep="")
print(a,b,c, sep=", ")
print(a,b,c, sep="\n")
# end -> 출력할 것을 전부 출력하고, 마지막에 값을 넣어줌
print(a, end=" ") # 줄바꿈이 되지 않고 한 칸 띄고 b가 출력됨
print(b)
print(c)



