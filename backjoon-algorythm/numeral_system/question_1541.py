# 잃어버린 괄호

import sys

calc = sys.stdin.readline().rstrip()
answer = 0

idx = 0
num_list = []
for i,v in enumerate(calc):
    if v=="-" or v=="+" :
        num_list.append(int(calc[idx:i]))
        num_list.append(v)
        idx = i+1
num_list.append(int(calc[idx:]))
#print(num_list)

include_minus = False
minus_idx = 0
for i in range(1,len(num_list),2):
    if num_list[i]=='-' :
        include_minus = True
        minus_idx = i
        break

if include_minus:
    for i in range(0,minus_idx,2):
        answer += num_list[i]
    for i in range(minus_idx+1, len(num_list),2):
        answer -= num_list[i]
else: # 전부 +인 경우
    for i in range(0,len(num_list),2):
        answer += num_list[i]

print(answer)
'''
minus = []
for i in range(1,len(num_list),2):
    if num_list[i]=='-' :
        minus.append(i)

if minus :
    minus.append(len(num_list))
#print(minus)

if not minus :
    for i in range(0,len(num_list),2) :
        answer += num_list[i]

else :
    for i in range(0,minus[0],2) :
        answer += num_list[i]
    for i in range(len(minus)-1) :
        for j in range(minus[i]+1, minus[i+1],2) :
            answer -= num_list[j]

print(answer)
'''