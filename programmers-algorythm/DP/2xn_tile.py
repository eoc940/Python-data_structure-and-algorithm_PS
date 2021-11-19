# 2 X N 타일링

def solution(n):
    answer = 0
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[0] = 1

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1000000007

    # print(dp)

    return dp[n]

n = 60000
print(solution(n))

# 마지막에 나눠주는 것보다 나눠서 개별로 넣어주는 것이 더 빠르다