# 땅따먹기



def solution(land):
    answer = 0
    dp = [[0]*len(land[0]) for _ in range(len(land))]
    for i in range(len(land[0])):
        dp[0][i] = land[0][i]
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] = land[i][j] + max([dp[i-1][k] for k in range(4) if k != j])
    #print(dp)

    return max(dp[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))