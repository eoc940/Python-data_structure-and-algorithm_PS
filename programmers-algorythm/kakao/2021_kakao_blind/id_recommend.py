# 신규 아이디 추천

def solution(new_id):

    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    special = ['-','_','.']
    for x in new_id :
        if x.isalpha() or x.isdigit() or x in special :
           answer += x

    # 3단계
    while '..' in answer :
        answer = answer.replace('..','.')

    # 나의 뻘짓코드
    # tmp2 = 's'
    # for x in new_id:
    #     if x=='.' and tmp2[-1]=='.' :
    #         continue
    #     else :
    #         tmp2 += x
    # answer = tmp2[1:]

    # 4단계
    if answer[0]=='.' :
        answer = answer[1:]
    if answer and answer[-1]=='.' :
        answer = answer[:-1]

    # 5단계
    if answer=='' :
        answer = 'a'

    # 6단계
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer.endswith('.') :
            answer = answer[:-1]

    # 7단계
    while len(answer) < 3 :
        answer += answer[-1]

    # 나의 뻘짓코드2
    # if len(answer) <= 2 :
    #     append_cnt = 3-len(answer)
    #     word = answer[-1]
    #     for i in range(append_cnt) :
    #         answer += word

    return answer

print(solution("z-+.^."))