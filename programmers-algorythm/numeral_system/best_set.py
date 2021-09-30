# 최고의 집합

def solution(n, s):

    avg = s/n
    if avg < 1:
        return [-1]

    left = s - int(avg)*n
    answer = [int(avg) for _ in range(n)]

    for i in range(left):
        answer[-(i+1)] += 1

    return answer

n,s = 2,1
print(solution(n,s))