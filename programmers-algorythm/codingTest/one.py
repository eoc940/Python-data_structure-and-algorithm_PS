def solution(s):
    answer = 0
    word_li = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8', 'nine':'9'}
    for key in word_li.keys() :
        if key in s : #해당 문자가 있는경우

            s=s.replace(key,word_li[key])


    answer = int(s)

    return answer

print(solution("123"))

