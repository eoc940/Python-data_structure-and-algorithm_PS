# 단어 찾기

# 문자열 find는 못찾았을때 -1 리턴, index는 못찾았을때 오류 발생

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
word = [sys.stdin.readline().rstrip() for _ in range(2*n-1)]
pair = defaultdict(int)

for x in word :
    pair[x] += 1

for k,v in pair.items() :
    if v==1 :
        print(k)





