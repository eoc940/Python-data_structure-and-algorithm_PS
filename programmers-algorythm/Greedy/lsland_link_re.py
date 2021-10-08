# 섬 연결하기

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    islands = set()
    islands.add(costs[0][0])
    while len(islands) < n:
        for is1, is2, cost in costs:
            if is1 in islands and is2 in islands:
                continue
            elif is1 in islands or is2 in islands:
                islands.add(is1)
                islands.add(is2)
                answer += cost
                break
    return answer
