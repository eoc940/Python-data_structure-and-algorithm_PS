# 네트워크

def solution(n, computers):
    answer = 0
    ch = [0] * n

    # dfs를 통해 자기자신외 연결된 컴퓨터들을 탐색하여 해당 인덱스 ch를 1로 바꿔줌
    def DFS(v) :
        for i in range(n) :
            # 조건식은 호출된 노드인 v와 다른컴퓨터 i와 연결되어있고,
            # v와 i는 다른 컴퓨터이고, 아직 한번도 지나지 않은 컴퓨터여야 함
            if computers[v][i]==1 and v!=i and ch[i]==0 :
                #체크를 먼저 해준후 다음 노드로 dfs호출
                ch[i]=1
                DFS(i)

    # 첫번째 컴퓨터는 당연히 ch가 0임. 따라서 첫 컴퓨터부터 dfs를 실행
    # 연결된 부분을 모두 체크한 후 answer(네트워크개수)에 1을 더해줌
    for i in range(n) :
        if ch[i]==0 :
            DFS(i)
            answer += 1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


