'''
리스트와 내장함수(1)
'''
import random as r

a=[] # 빈 리스트를 만든는 방법 1
print(a)
b=list() # 빈 리스트를 만든는 방법 2
print(b)

a=[1,2,3,4,5]
print(a)
print(a[0])

b=list(range(1,11))
print(b)

c=a+b  # 리스트 덧셈연산이 가능. 연산은 순서대로!
print(c)

print(a)

a.append(6)
print(a)

a.pop()
print(a)

a.insert(3, 7) # 3번 인덱스에 7을 넣어라
print(a)

a.pop(3) # 3번 인덱스를 pop하라
print(a)

a.append(4)
print(a)

a.remove(4) # 4라는 값을 찾아서 제거(첫번째 4만 제거됨)
print(a)

print(a.index(5))

a=list(range(1,11))
print(a)

print(sum(a)) # a라는 리스트의 합을 출력

print(max(a)) # a리스트 안의 최대값 출력

print(min(a)) # a리스트 안의 최소값 출력

print(min(7,5)) # 7과 5중 최소값을 출력

print(a)
r.shuffle(a)
print(a)

a.sort() # 오름차순 정렬
print(a)

a.sort(reverse=True) # 내림차순 정렬
print(a)

a.clear() # 리스트를 비워버림
print(a)

a=[23,12,36,53,19]
print(a[:3]) # 0-2 인덱스 출력
print(a[1:4]) # 1-3 인덱스 출력
print(len(a))

for i in range(len(a)) :
    print(a[i], end=" ")
print()

for x in a :  # a리스트에서 하나씩 빼옴
    print(x, end=" ")
print()

for x in a :
    if x%2==1 :
        print(x, end=" ")
print()

for x in enumerate(a) :  # 인덱스와 값이 매핑되어 튜플로 출력
    print(x, end=" ")
print()

b=(1,2,3,4,5)  # 튜플
print(b)
# b[0] = 7 -> 이렇게 값 변경 불가능
print(b[0])

for x in enumerate(a) :
    print(x[0], x[1])
print()

for index, value in enumerate(a) :
    print(index, value)
print()

# a에 있는 요소들 모두가 50이하이면 true
if all(50>x for x in a) :
    print("Yes")
else:
    print("No")

# a에 있는 요소들 중 하나가 50이하이면 true
if any(50>x for x in a) :
    print("Yes")
else:
    print("No")




