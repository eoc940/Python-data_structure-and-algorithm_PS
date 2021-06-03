# 동전 바꿔주기(dfs)
# 동전 종류 개수를 인덱스 겸 레벨(v)로 삼는다
# 동전 전부 거친 뒤 total이 같은 것을 센다
import sys

T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coin = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
coin.sort(reverse=True)

def dfs(v, tot) :
    global cnt
    if tot > T :
        return
    if v==k :
        if tot==T :
            cnt += 1
            return
    else :
        for i in range(coin[v][1]+1) :
            #print(v)
            dfs(v+1, tot+coin[v][0]*i)


cnt = 0
dfs(0,0)
print(cnt)




