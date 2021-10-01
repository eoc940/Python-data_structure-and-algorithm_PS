# 야근 지수

import heapq

def solution(n, works):
    answer = 0

    heap_list = []
    for work in works:
        heapq.heappush(heap_list, -work)

    while n > 0:
        min_num = heapq.heappop(heap_list)
        min_num += 1
        heapq.heappush(heap_list, min_num)
        n -= 1

    for num in heap_list:
        if num < 0:
            answer += num**2

    print(heap_list)

    return answer

n = 3
works = [1,1]
print(solution(n, works))

# 최댓값이나 최솟값을 하나씩 빼서 풀어야 한다는 생각이 들면 힙을 이용하자





