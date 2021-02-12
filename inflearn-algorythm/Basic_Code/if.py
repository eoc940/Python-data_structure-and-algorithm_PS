'''
조건문 if(분기, 중첩)

# 단일 if
x=7
if x==7 :
    print("Lucky")
    print("zzzz")
if x!=8 :
    print("ggg")


#중첩 if
x=15
if x>10 :
    if x%2==1 :
        print("10이상의 홀수다")
x=7
if x>0 and x<10 :
    print("10보다 작은 자연수")

x=7
if 0<x<10 : # 파이썬은 부등호 2개 가이 사용가능!!
    print("10보다 작은 자연수")


x=10
if x>0 :
    print("+")
else:
    print("-")
'''

x=76
if x >= 90 :
    print("A")
elif x >= 80 :
    print("B")
elif x >= 70 :
    print("C")
else:
    print("F")



