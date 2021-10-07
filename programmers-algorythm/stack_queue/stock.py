def solution(prices):
    answer = [0] * len(prices)
    stk = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer[i] = cnt

    return answer