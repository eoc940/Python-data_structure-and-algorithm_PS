# 거스름돈
# 0 1 2 3 4 5
# 1 0 1 1 1 1
def solution(n, money):
    money.sort()
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for coin in money:
        for i in range(coin, len(dp)):
            dp[i] += dp[i-coin]
        # print(dp)

    return dp[n]

n = 5
money = [1,2,5]
print(solution(n, money))
