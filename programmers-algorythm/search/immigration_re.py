# 입국심사

def solution(n, times):
    answer = 0
    lt = 0
    rt = max(times) * n

    while lt <= rt:
        mid = (lt + rt) // 2
        people = 0
        for time in times:
            people += mid // time

        if people < n:
            lt = mid + 1
        else:
            rt = mid - 1
            answer = mid

    return answer

