# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    _min = min(n,m)
    for i in range(_min,0,-1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    _max = max(n,m)
    for i in range(_max, n*m+1):
        if i%n==0 and i%m==0:
            answer.append(i)
            break
    return answer

n,m = 2,5
print(solution(n,m))