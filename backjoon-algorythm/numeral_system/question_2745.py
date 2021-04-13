# 진법 변환
import sys

num, zin = sys.stdin.readline().split()
zin = int(zin)

mapping = dict()
for i in range(10) :
    mapping[str(i)] = i

for i in range(10,36) :
    mapping[chr(55+i)] = i

result = 0

for j in range(len(num)) :
    result += mapping.get(num[j])*zin**(len(num)-1-j)
print(result)





