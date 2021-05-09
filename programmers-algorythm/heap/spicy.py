# 더 맵게
import heapq

def solution(scoville, K):
    answer = 0

    heap_scoville = heapq.heapify(scoville)

    while scoville[0] < K : #min(scoville)을 쓰니까 시간초과가 났다.
        print(scoville)
        if len(scoville)==1 :
            answer = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        answer += 1


    return answer

print(solution([1,2,3,9,10,12],7))