# 동전교환(냅색알고리즘)

import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
change = int(sys.stdin.readline())
dy = [0] * (change+1)

coins.sort()
init_val = coins[0]
for i in range(init_val, change+1) :
    dy[i] = dy[i-init_val] + 1

for i in range(1, n) :
    val = coins[i]
    for j in range(val, change+1) :
        dy[j] = min(dy[j], dy[j-val] + 1)

print(dy[change])

# 강사님 풀이
'''
나는 init을 해주느라 제일 작은 동전으로 먼저 dy를 채웠는데
강사님은 큰값으로 미리 넣고 시작했다.
'''
import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
change = int(sys.stdin.readline())
dy = [float('inf')] * (change+1)
dy[0] = 0

for i in range(n) :
    val = coins[i]
    for j in range(val, change+1) :
        dy[j] = min(dy[j], dy[j-val] + 1)

print(dy[change])

