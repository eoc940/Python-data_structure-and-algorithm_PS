# 교육과정 설계

from collections import deque

essential = input()
n = int(input())
subjects = [input() for _ in range(n)]

for i in range(n) :
    idx = 0
    que = []
    que = deque(que)
    for j in range(len(subjects[i])):
        if subjects[i][j] in essential:
            if subjects[i][j] not in que:
                que.append(subjects[i][j])
            else:
                continue
    if ''.join(que) == essential:
        print("#%d" % (i + 1), "YES")
    else:
        print("#%d" % (i + 1), "NO")

# 강사님 풀이

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))







