# 최대힙

# heapq는 최소힙으로 작동하는데
# 각각의 노드에 -1을 곱한 뒤
# 나중에 값이 필요할 때 다시 -1을 곱하면 최대힙을 구현할 수 있다.
import heapq as hq

a = []
while True :
    n = int(input()) * (-1)
    if n == 1 :
        break
    if n == 0 :
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a) * (-1))
    else :
        hq.heappush(a, n)#a라는 리스트에 n값을 push한다

# 다른 풀이

a = []
while True :
    n = int(input())
    if n == -1 :
        break
    if n == 0 :
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else :
        hq.heappush(a, -n)#a라는 리스트에 -n값을 push한다