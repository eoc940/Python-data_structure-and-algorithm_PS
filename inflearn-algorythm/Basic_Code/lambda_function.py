'''
람다 함수(익명의 함수, 혹은 표현식)

def plus_one(x) :
    return x+1
print(plus_one(1))

plus_two=lambda x : x+2 # 좌측 변수에 우측 람다식을 넣으면 함수처럼 이용가능
print(plus_two(1))
'''

def plus_one(x) :
    return x+1
a=[1,2,3]
print(list(map(plus_one, a)))
# map의 첫번째는 함수, 두번째는 자료
# 위는 a라는 리스트에 plus_one을 적용시키라는 의미

print(list(map(lambda x : x+1,a)))
# 위와 같은 기능을 함. 람다식으로 표현




