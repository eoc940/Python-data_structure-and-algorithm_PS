# 교육과정 설계

import sys

must = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
example = [sys.stdin.readline().rstrip() for _ in range(n)]
idx = 0
for x in example :
    order = -1
    idx += 1
    flag = True
    for y in must :
        if order < x.find(y) :
            order = x.find(y)
        else :
            flag = False
            break
    # 출력부
    if flag :
        print("#%d YES" % (idx))
    else :
        print("#%d NO" % (idx))









