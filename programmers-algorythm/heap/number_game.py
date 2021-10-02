# 숫자 게임
# 리스트가 이미 생성되어 있는 상태에서 heappop을 해버리면 힙 정렬 안된상태에서 pop된다
# heappush, heappop을 쓸 경우 힙 정렬이 되기 때문에 만약 heappush를 한번 하고 나서
# heappop을 쓰면 문제없지만 그런 걸 쓰지 않은 상태에서 heappop하면 잘못된 결과가 나오므로
# heappop을 먼저 써야 할 경우 heapify를 먼저 해 주어야 한다

import heapq

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    heapq.heapify(B)
    print(A,B)
    while B:
        b = heapq.heappop(B)
        print(b, A[-1])
        if b > A[-1]:
            answer += 1
            A.pop()
    return answer

A = [1,2,3]
B = [3,2,1]
print(solution(A,B))


