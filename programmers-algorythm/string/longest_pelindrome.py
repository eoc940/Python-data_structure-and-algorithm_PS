# 가장 긴 펠린드롬


def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(len(s)-1, i-1, -1):
            tmp = s[i:j + 1]
            if len(tmp) <= answer:
                break
            if tmp == tmp[::-1]:
                answer = len(tmp)

    return answer

s = "abcbea"
print(solution(s))