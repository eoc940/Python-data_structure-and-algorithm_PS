# 이중우선순위큐
import heapq

def solution(operations):
    answer = []
    heap = []
    heapq.heapify(heap)
    for x in operations :
        comm = x.split()
        if comm[0] == 'I' : # 숫자 삽입
            heapq.heappush(heap, int(comm[1]))
        else : # 삭제
            if not heap :
                continue
            if comm[1] == '-1' :
                heapq.heappop(heap)
            else :
                # 최대힙
                tmp = []
                for y in heap :
                    heapq.heappush(tmp, (-y,y))
                heap.remove(heapq.heappop(tmp)[1])
    if not heap :
        answer = [0,0]
    else :
        answer.append(max(heap))
        answer.append(heap[0])
    return answer

operation = ["I 7","I 5","I -5","D -1"]
print(solution(operation))