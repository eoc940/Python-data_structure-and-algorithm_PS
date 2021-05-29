# 아나그램

import sys
from collections import defaultdict

n1 = sys.stdin.readline().rstrip()
n2 = sys.stdin.readline().rstrip()

dict1 = defaultdict(int)
dict2 = defaultdict(int)

for i in range(len(n1)) :
    dict1[n1[i]] += 1
    dict2[n2[i]] += 1

for k,v in dict1.items() :
    if dict2[k] != v:
        print("NO")
        break
else :
    print("YES")






