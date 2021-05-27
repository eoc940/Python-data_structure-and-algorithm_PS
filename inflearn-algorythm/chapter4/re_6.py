# 씨름 선수(그리디)

import sys

n = int(sys.stdin.readline())
info = []
for i in range(n) :
    hei, wei = map(int, sys.stdin.readline().split())
    info.append((hei,wei))

info.sort(key=lambda x : (x[0],x[1]))
cnt = 0
for i in range(len(info)) :
    for j in range(i, len(info)) :
        if info[i][1] < info[j][1] :
            break
    else :
        cnt += 1

print(cnt)



