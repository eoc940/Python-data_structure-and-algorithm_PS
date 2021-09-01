def solution(word):
    answer = 0
    alpha = {"A":1,"E":2,"I":3,"O":4,"U":5}
    li_word = [alpha[i] for i in word]
    #print(li_word)

    cur = []

    while True:
        #print(cur, answer)
        if li_word == cur:
            return answer
        if len(cur) < 5:
            cur.append(1)

        else: # cur 길이가 5가 될때
            if cur[-1] == 5: # 길이 5이고 마지막 값이 5
                # 뒤에서부터 5가 아닌 것을 찾아서 숫자를 1 올림
                for i in range(4,-1,-1):
                    if cur[i] != 5:
                        for _ in range(4-i):
                            cur.pop()
                        cur[i] += 1
                        break
            else: # 길이 5이고 마지막 값이 5가 아님
                cur[-1] += 1
        answer += 1





word = "EIO"
print(solution(word))