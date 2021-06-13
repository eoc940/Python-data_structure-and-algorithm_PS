# 사다리 타기(dfs)

import sys

ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
answer = 0


def dfs(v, num) :
    global answer
    if v==0 :

        answer = num
        return
    else :

        if num-1 >= 0 and ladder[v][num-1] == 1 :
            ladder[v][num] = 0
            dfs(v, num-1)
        elif num+1 <= 9 and ladder[v][num+1] == 1 :
            ladder[v][num] = 0
            dfs(v, num+1)
        elif ladder[v-1][num] == 1:
            ladder[v][num] = 0
            dfs(v-1, num)


for i, x in enumerate(ladder[9]) :
    if x == 2 :

        dfs(9,i)

print(answer)



