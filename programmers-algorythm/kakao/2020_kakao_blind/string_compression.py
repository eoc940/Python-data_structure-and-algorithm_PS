# 문자열 압축

from collections import deque

def compression(strings):
    current = ""
    cnt = 0
    print(strings)
    strings = deque(strings)
    result = []
    while strings:
        val = strings.popleft()
        if not result:
            result.append([val,1])
        else:
            if result[-1][0] == val:
                result[-1][1] += 1
            else:
                result.append([val, 1])
    print(result)
    compress = ""
    for res in result:
        char, repeat = res
        if repeat == 1:
            compress += char
        elif repeat > 1:
            compress += str(repeat) + char

    print(compress)
    print()
    return len(compress)


def solution(s):
    answer = float('inf')
    if len(s) == 1:
        return 1

    for i in range(1, len(s)):
        strings = []
        for j in range(0, len(s), i):
            strings.append(s[j:j+i])
        answer = min(answer, compression(strings))
    return answer

s = "a"
print(solution(s))
