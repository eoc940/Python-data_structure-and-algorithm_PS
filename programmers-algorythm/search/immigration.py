# 입국심사

def solution(n, times):
    answer = 0
    lt = 1
    rt = max(times) * n

    while lt <= rt :
        mid = (lt + rt) // 2
        count = 0
        for i in times :
            count += mid//i
            if count >= n :
                break

        if count>=n :
            answer = mid
            rt = mid - 1
        else :
            lt = mid + 1

    return answer
print(solution(6,[7,10]))