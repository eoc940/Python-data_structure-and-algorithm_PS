def solution(s):
    answer = ''
    word_list = s.split(" ")
    print(word_list)
    for idx, word in enumerate(word_list):
        word = word.lower()
        if word == "":
            answer += " "
        else:
            answer += word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper()
            answer += " "
    answer = answer[:-1]
    return answer

s = "  aa bb  cc "
print(solution(s))

