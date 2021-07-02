# 수식 최대화

from itertools import permutations
import copy

def calculate(num1, num2, oper):
    if oper=="-":
        return int(num1)-int(num2)
    elif oper=="+":
        return int(num1)+int(num2)
    else :
        return int(num1)*int(num2)


def solution(expression):
    answer = 0
    operator = []
    operator_set = set()
    for i,v in enumerate(expression):
        if v in ["+", "-", "*"]:
            operator.append(i)
            operator_set.add(v)
    values = []

    idx = 0
    for x in operator:
        values.append(expression[idx:x])
        values.append(expression[x])
        idx = x+1
    values.append(expression[x+1:])
    # print(values)
    operator_list = list(operator_set)
    # print(operator_list)
    operator_prior = permutations(operator_list, len(operator_list))
    # print(list(operator_prior))
    for oper_opt in operator_prior:
        num_and_oper = copy.deepcopy(values)
        for oper in oper_opt :
            while True:
                try :
                    idx = num_and_oper.index(oper)
                    calculated = calculate(num_and_oper[idx-1], num_and_oper[idx+1], oper)
                    # print(oper,idx, calculated)
                    for _ in range(3):
                        del num_and_oper[idx-1]
                    num_and_oper.insert(idx-1, calculated)
                except:
                    break
        # print(oper_opt, num_and_oper)
        answer = max(answer, abs(int(num_and_oper[0])))


    return answer

expression = "100-200*300-500+20"
print(solution(expression))

# 다른 풀이
# https://jokerldg.github.io/algorithm/2021/05/19/maximize-expression.html

# a=["*","2","4"]
# print(a.find("2"))

