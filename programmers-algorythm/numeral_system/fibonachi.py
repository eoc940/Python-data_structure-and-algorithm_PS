# 피보나치의 수

def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    if n <= 1: return dp[n]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    #print(dp)

    return dp[n]%1234567

print(solution(1))