# 이중우선순위큐
import heapq
# heap은 push, pop할때 자동 정렬됨
def solution(operations):
    answer = []
    # 값들을 넣어줄 heap 리스트를 만든다. 이 리스트를 heap으로 만드는데
    # 여기서는 써도되고 안써도되고 밑에 heappush를 하면 heap이 된다
    heap = []
    heapq.heapify(heap)
    # 매개변수 operations를 반복문으로 돌려 분류한다
    for x in operations :
        # comm[0]은 값 삽입/삭제 여부, comm[1]은 값
        comm = x.split()
        if comm[0] == 'I' : # 숫자 삽입 명령
            # heap이라는 리스트를 heapq자료형으로 하고 값을 push해준다.
            # push되면 힙 자료구조로 자동 정렬된다
            heapq.heappush(heap, int(comm[1]))
        else : # 삭제 명령
            # 문제에서 값이 없을때 삭제 명령을 받으면 진행하지 않는다고 했다
            if not heap :
                continue
            # 값이 -1이면 최소값을 삭제하라는 명령이다
            # heappop을 써주면 최소값이 pop된다
            if comm[1] == '-1' :
                heapq.heappop(heap)
            # else는 값이 1이 들어온 경우이다
            # 이때는 최대힙을 만든 뒤 pop시키면 된다
            else :
                # 최대힙(tmp)
                tmp = []
                for y in heap :
                    # -y가 우선순위로 들어가므로 y는 가장 큰 값 순으로 정렬된다
                    heapq.heappush(tmp, (-y,y))
                # (-y,y) 튜플에서 인덱스 1 즉 y의 값을 뽑은 후 heap에서 remove한다
                heap.remove(heapq.heappop(tmp)[1])
    # heap리스트에 값이 없으면 [0,0]
    if not heap :
        answer = [0,0]
    # heap리스트에 값이 있으면 최대값과 최소값을 append
    else :
        answer.append(max(heap))
        answer.append(heap[0])
    return answer

operation = ["I 7","I 5","I -5","D -1"]
print(solution(operation))