# 동전교환(DFS)

import sys
n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))
val = int(sys.stdin.readline())

coin.sort(reverse=True)

def dfs(count, total) :
    global mini
    #print(count,total, mini)
    if total > val :
        return
    if count >= mini :
        return

    if total == val :
        # if count < mini :
        #     mini = count
        mini = count

    else :
        for x in coin :
            dfs(count+1, total+x)

mini = float('inf')
dfs(0,0)
print(mini)


