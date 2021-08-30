def solution(numOfStairs):
    answer = 0
    dp = [0] * (numOfStairs + 1)
    if numOfStairs == 1:
        return 1
    elif numOfStairs == 2:
        return 2
    elif numOfStairs == 3:
        return 4
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, numOfStairs + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp)
    return dp[numOfStairs]

print(solution(5))