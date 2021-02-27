# 침몰하는 타이타닉(그리디)

n, boat = map(int, input().split())
man = list(map(int, input().split()))

man.sort(reverse=True)
cnt = 0
while len(man) > 0 :
    if man[0] + man[-1] <= boat :
        del man[0]
        if len(man)!=0 :
            del man[-1]
        cnt += 1
    else:
        del man[0]
        cnt += 1
print(cnt)

# 강사님 풀이

n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
cnt = 0
while p: # p가 비어있으면 거짓이 되어 반복문 종료
    if len(p)==1 :
        cnt += 1
        break
    if p[0] + p[-1] > limit :
        p.pop() # 맨 뒤 사라지게 함
        cnt += 1
    else:
        p.pop(0)
        p.pop()
        cnt += 1
print(cnt)

# deque 이용 방법

from collections import deque

n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p = deque(p)
cnt = 0
while p: # p가 비어있으면 거짓이 되어 반복문 종료
    if len(p)==1 :
        cnt += 1
        break
    if p[0] + p[-1] > limit :
        p.pop() # 맨 뒤 사라지게 함
        cnt += 1
    else:
        p.popleft() # deque쓰면 맨 앞 pop할때 이거 씀
        p.pop()
        cnt += 1
print(cnt)