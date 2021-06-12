# 발차기

import sys

n = int(sys.stdin.readline())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def dfs(my, rival, L) :
    global answer
    if my > rival:
        return
    if my == rival :
        if answer > L :
            answer = L
    else :
        dfs(my*2, rival+3, L+1)
        dfs(my+1, rival, L+1)

for x in scores :
    answer = float('inf')
    dfs(x[0], x[1], 0)
    print(answer)
