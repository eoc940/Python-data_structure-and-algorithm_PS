# 짝지어 제거하기


def solution(s):

    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        else: # stack에 원소가 있을 경우
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    # print(stack)
    if stack:
        return 0
    return 1

s = "cdcd"
print(solution(s))

