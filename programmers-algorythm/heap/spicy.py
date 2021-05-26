# 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    # scoville 리스트를 heap(우선순위큐)로 만들어줌
    heapq.heapify(scoville)

    # scoville의 맨 앞의 값이 K이하이면 계속 반복 돌림
    while scoville[0] < K : #min(scoville)을 쓰니까 시간초과가 났다.
        # 스코빌 지수를 K이상으로 만들 수 없는 경우에 -1리턴
        if len(scoville)==1 :
            answer = -1
            break
        # 스코빌 지수 만들기 : 맨앞에서 pop하고 그 다음 pop해서 2를 곱한 뒤 더한다
        heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        # 횟수를 1 증가시킴
        answer += 1

    return answer

print(solution([2,1,12,9,10,3],7))


