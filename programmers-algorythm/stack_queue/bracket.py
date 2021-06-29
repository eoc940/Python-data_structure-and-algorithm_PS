# 올바른 괄호
def solution(s):

    st = []

    for x in s:
        if x=="(" :
            st.append("(")
        else :
            try :
                st.pop()
            except:
                return False
    if not st:
        return True
    else:
        return False


s = ")()("
print(solution(s))