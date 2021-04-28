# 괄호 변환

def solution(p):
    open = 0
    close = 0
    right = True
    if p=="" :
        return ""

    for x in p :
        if x=="(" :
            open += 1
        else :
            close += 1
        if open < close :
            right = False
        if open == close :
            if right :
                return p[:open+close] + solution(p[open+close:])
            else : #올바른 괄호 문자열이 아님
                convert = ""
                convert += "("
                convert += solution(p[open + close:])
                convert += ")"
                tmp = p[:open+close]
                remove_fb = tmp[1:len(tmp) - 1]
                for y in remove_fb :
                    if y=="(" :
                        convert += ")"
                    else:
                        convert += "("
                return convert

print(solution("(()())()"))