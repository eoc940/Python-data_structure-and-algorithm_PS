# 예상 대진표

def is_match(a,b):
    if abs(a-b)==1 and max(a,b)%2 == 0:
        return True
    return False


def solution(n,a,b):
    answer = 1

    while n > 1:
        # print(a,b)
        if is_match(a,b):
            break
        answer += 1
        n //= 2
        if a%2 == 1: a += 1
        if b%2 == 1: b += 1
        a //= 2
        b //= 2

    return answer


n,a,b = 16,7,6
print(solution(n,a,b))



