# 스도쿠 검사

import sys
from itertools import product

st = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

flag = True

for i in range(9) :
    ch = {1:False, 2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
    for j in range(9) :
        ch[st[i][j]] = True

    if False in ch.values() :
        flag = False
        break
#print(flag)
for i in range(9) :
    ch = {1:False, 2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
    for j in range(9) :
        ch[st[j][i]] = True
    if False in ch.values() :
        flag = False
        break
#print(flag)
dist = [0,3,6]
dist_pair = product(dist, repeat=2)
for x in dist_pair :
    ch = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
    #print(x[0],x[1])
    for i in range(x[0],x[0] + 3) :
        for j in range(x[1],x[1] + 3) :
            #print(i,j, end="  ")
            ch[st[i][j]] = True
        #print()
    if False in ch.values() :
        flag = False
        break

#print(flag)

if flag :
    print("YES")
else :
    print("NO")