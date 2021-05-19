# 숫자만 추출

import sys

word = sys.stdin.readline()
nums = []

for x in word :
    if x.isdigit() :
        nums.append(x)

answer = int(''.join(nums))

yaksoo = 0
for i in range(1,answer+1) :
    if answer%i==0 :
        yaksoo += 1

print(answer)
print(yaksoo)
