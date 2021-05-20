# 사과나무(다이아몬드)

import sys
n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mid = n//2
total = 0
step = 0
for i in range(n//2) :
    total += sum(tree[i][mid - step:mid + 1 + step])
    #print(tree[i][mid - step:mid + 1 + step])
    step += 1
for i in range(n//2, n) :
    total += sum(tree[i][mid - step:mid + 1 + step])
    #print(tree[i][mid - step:mid + 1 + step])
    step -= 1
print(total)

