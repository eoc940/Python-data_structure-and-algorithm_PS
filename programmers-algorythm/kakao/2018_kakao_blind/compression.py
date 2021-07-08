# 압축

def solution(msg):
    answer = []
    dic = dict()
    for i in range(26):
        dic[chr(i+65)] = i+1
    idx = 0
    word = ""
    while True:
        word += msg[idx]
        if word in dic.keys():
            idx += 1
            if idx==len(msg):
                answer.append(dic[word])
                break
            continue
        else :
            answer.append(dic[word[:-1]])
            dic[word] = len(dic) + 1
            word = ""

    return answer

msg = "ABABABABABABABAB"
print(solution(msg))
