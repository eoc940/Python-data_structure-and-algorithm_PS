# 섬 연결하기

def solution(n, costs):
    answer = 0
    island = set()
    island.add(costs[2][0]) # 아무거나 넣어도됨 0~n-1 중에
    # 거리를 기준으로 오름차순으로 정렬한다
    costs.sort(key=lambda x : x[2])
    cnt = 0
    # island라는 set에 모든 섬 번호가 들어오면 반복문 종료
    while len(island) != n :
        # 섬 정보를 반복문 돌린다
        for x in costs :
            std, end, cost = x[0],x[1],x[2]
            # 출발, 도착 섬 모두 이미 island에 있다면 continue
            if std in island and end in island :
                continue
            # 출발, 도착 중 하나만 island에 있다면 둘다 set에 넣는다
            # 그리고 answer에 거리를 더해주고 break한다
            # 왜냐하면 하나의 연결을 완료했기 때문에 다시 탐색해야 한다
            elif std in island or end in island :
                island.update([std, end])
                answer += cost
                break

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))

