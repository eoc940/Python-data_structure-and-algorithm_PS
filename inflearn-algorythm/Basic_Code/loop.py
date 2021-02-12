'''
반복문(for, while)
a = range(10)
print(list(a))

a = range(1,11)
print(list(a))

for i in range(10) :
    print("Hello")
# 감소 for문 실행하고 싶으면 맨 뒤에 인자 하나 더 넣어야함
for i in range(10,0, -1) :
    print(i)

for i in range(10, 0, -2):
     print(i)

i=1
while i<=10 :
    print(i)
    i += 1
i=10
while i>=1 :
    print(i)
    i -= 1
i=1
while True :
    print(i)
    if i==10 :
        break  # 어느 순간에 반복을 멈추고 싶을 때
    i+=1

for i in range(1,11) :
    if i%2==0 :
        continue # 반복에서 필터를 하고 싶을 때
    print(i)
'''
# for-else구문
# for문 안에 break당해버리면 else 실행 안함
# break 안당하면 else도 정상실행됨
for i in range(1,11) :
    print(i)
    if i==15 :
        break
else :
    print(11)








