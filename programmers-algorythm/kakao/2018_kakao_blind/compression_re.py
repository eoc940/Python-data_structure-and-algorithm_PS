# 압축

def solution(msg):
    answer = []
    alpha = {chr(65 + i) : i + 1 for i in range(26)}
    # print(alpha)
    st = 0
    len_alpha = len(alpha)
    for i in range(st, len(msg)):
        word = msg[st:i + 1]
        if word not in alpha.keys():
            len_alpha += 1
            alpha[word] = len_alpha
            answer.append(alpha[word[:-1]])
            st = i
    answer.append(alpha[msg[st:]])

    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))


