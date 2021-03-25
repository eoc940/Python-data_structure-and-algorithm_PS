# 주식 가격

def solution(prices):
    answer = []
    for i in range(len(prices)) :
        tmp = []
        for j in range(i+1,len(prices)) :
            tmp.append(1)
            if prices[i] <= prices[j] :
                continue
            else :
                break
        answer.append(sum(tmp))

    return answer

print(solution([1,2,3,2,3]))
