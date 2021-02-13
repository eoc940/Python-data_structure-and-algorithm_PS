'''
함수 만들기
# 함수는 메인스크립트 위에 만들어놔야 한다.
def add(a,b) :
    c = a+b
    print(c)

add(3,4)

def add(a,b) :
    c=a+b
    return c

print(add(5,2))

def add(a,b) :
    c=a+b
    d=a-b
    return c, d  # 값 여러개 리턴 가능(튜플로 리턴됨)

print(add(3,5))
'''

def isPrime(x) :
    for i in range(2,x) :
        if x%i==0 :
            return False
    return True

a=[12,13,7,9,19]

for x in a :
    if isPrime(x)==True :
        print(x, end=" ")






