# 괄호 회전하기

def convert(s, i):
    return s[i:] + s[:i]

def validate(s):
    stack = []
    for bracket in s:
        if bracket in ["(", "{", "["]:
            stack.append(bracket)
        else:
            if not stack:
                return 0
            if stack and stack[-1] == "(" and bracket == ")":
                stack.pop()
            elif stack and stack[-1] == "{" and bracket == "}":
                stack.pop()
            elif stack and stack[-1] == "[" and bracket == "]":
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1

    else: return 0


def solution(s):
    answer = 0

    for i in range(len(s)):
        bracket = convert(s, i)

        answer += validate(bracket)
    return answer

s = "[(){}}}())"
print(solution(s))