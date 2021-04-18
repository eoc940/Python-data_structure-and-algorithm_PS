# 가방문제(냅색 알고리즘)
'''
냅색 알고리즘
이 문제에서 여러 보석이 있는데 한 보석이 있다고만 가정하고 진행한다.
dy리스트에서 dy[i]의 의미는 가방의 무게가 i일때 담을 수 있는 최대 가치를
의미하는 것이다. 현재 보석의 무게가 w이라면 dy[i] 즉 무게가 i일때 최대
가치를 측정하고 싶을때 dy[i] == dy[i-w] + value(w)일 것이다.
이렇게 한 가지 보석으로 전체 dy리스트의 각 인덱스 값들을 넣어주고 그 다음
다른 한 보석이 있다고만 가정하고 dy를 채워나가는데, 기존의 dy의 값보다 더
커졌을 경우, 큰 값으로 업데이트한다.
'''

import sys


n, w = map(int, sys.stdin.readline().split())
info = []
for i in range(n) :
    weight, value = map(int, sys.stdin.readline().split())
    info.append((weight,value))

dy = [0]*(w+1)
for j in range(n) :
    wei = info[j][0]
    val = info[j][1]
    for k in range(wei, w+1) :
        if dy[k-wei] + val > dy[k] :
            dy[k] = dy[k-wei] + val

print(dy[w])




