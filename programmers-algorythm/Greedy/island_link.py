# 섬 연결하기

def solution(n, costs):
    answer = 0
    island = set()
    island.add(costs[2][0]) # 아무거나 넣어도됨 0~n-1 중에
    costs.sort(key=lambda x : x[2])
    cnt = 0
    while len(island) != n :

        for x in costs :
            std, end, cost = x[0],x[1],x[2]
            if std in island and end in island :
                continue
            elif std in island or end in island :
                island.update([std, end])
                answer += cost
                break

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))

