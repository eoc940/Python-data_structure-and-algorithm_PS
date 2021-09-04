# 올바른 괄호

def solution(s):
    answer = True
    bracket = 0
    for x in s:
        if x == "(": bracket += 1
        else: bracket -= 1
        if bracket < 0: return False
    return bracket == 0

s = "(()("
print(solution(s))