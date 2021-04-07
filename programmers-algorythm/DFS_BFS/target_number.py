# 타겟 넘버

def solution(numbers, target):
    global answer
    answer = 0
    def DFS(L, sum):
        global answer
        if L == len(numbers):
            if sum==target :
                answer += 1
        else :
            DFS(L+1, sum+numbers[L])
            DFS(L+1, sum-numbers[L])
    DFS(0, 0)
    return answer

s = solution([1,1,1,1,1],3)
print(s)






