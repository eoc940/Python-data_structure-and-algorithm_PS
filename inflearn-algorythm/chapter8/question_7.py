# 가장 높은 탑 쌓기

import sys
from operator import itemgetter

n = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = [0]*(n+1)
# sort는 첫번째 자료로 sort, 그후 두번째 자료로 sort 이런식으로 하므로
# 여기서는 info.sort(reverse=True)만 해도 된다.
info.sort(key=itemgetter(0), reverse=True)
info.insert(0,[0,0,0])
dy[1] = info[1][1]

for i in range(2, n+1) :
    val = 0
    for j in range(1, i) :
        if info[i][2] < info[j][2] and dy[j] > val :
            val = dy[j]
    dy[i] = val+info[i][1]

print(max(dy))
