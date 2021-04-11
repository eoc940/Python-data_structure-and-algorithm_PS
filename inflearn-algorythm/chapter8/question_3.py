# 계단오르기 top-down 메모이제이션
'''
사실 엄연히 동적계획법은 bottom-up 방식임
top-down 방식은 넓은 의미에서 동적계획법임
'''

import sys

def DFS(v) :
    if ch[v] > 0 :
        return ch[v]

    if v==1 or v==2 :
        ch[v] = v
        return ch[v]
    else :
        ch[v] = DFS(v-1) + DFS(v-2)
        return ch[v]

n = int(sys.stdin.readline())
ch = [0]*(n+1)
print(DFS(n))



