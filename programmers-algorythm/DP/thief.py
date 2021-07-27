# 도둑질

def solution(money):
    answer = 0
    dp1 = [0]*len(money)
    # print(money)
    dp1[0] = money[0] # 첫 집을 무조건 턴다
    dp1[1] = max(money[0], money[1])
    for i in range(2,len(dp1)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    # print(dp1)
    dp2 = [0]*len(money)
    dp2[0] = 0
    dp2[1] = money[1] # 첫 집을 털지 않고 두번째 집을 턴다
    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    # print(dp2)

    return max(dp1[len(dp1)-2], dp2[len(dp2)-1])

money = [1,2,3,5]
print(solution(money))

