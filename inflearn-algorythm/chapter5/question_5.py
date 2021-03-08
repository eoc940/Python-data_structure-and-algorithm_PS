# 공주 구하기(큐 자료구조로 해결)

n, k = map(int, input().split())

nums = [x+1 for x in range(n)]

cnt = 0
while len(nums) > 1 :
    cnt += 1
    if cnt == k :
        nums.pop(0)
        cnt = 0
    else:
        nums.append(nums.pop(0))

print(nums.pop())

# 강사님 풀이

from collections import deque
n, k = map(int, input().split())
dq = list(range(1,n+1))
print(dq)
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()



