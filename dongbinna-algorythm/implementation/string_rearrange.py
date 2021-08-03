# 문자열 재정렬

import sys
string = list(sys.stdin.readline().rstrip())
alpha_list = []
number = 0
answer = ''
for word in string:
    if word.isalpha(): alpha_list.append(word)
    elif word.isdigit(): number += int(word)

alpha_list.sort()
answer = ''.join(alpha_list) + str(number)
print(answer)