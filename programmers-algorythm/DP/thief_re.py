# 도둑질

def solution(money):
    answer = 0
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]

    # 첫번째 집 터는 경우
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫번째 집 털지 않는 경우
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(max(dp1), max(dp2))


