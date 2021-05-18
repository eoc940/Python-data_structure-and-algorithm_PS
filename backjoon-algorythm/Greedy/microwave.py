# 전자레인지

import sys

n = int(sys.stdin.readline())
count_dict = dict()
count_dict['A'] = 0
count_dict['B'] = 0
count_dict['C'] = 0

if n%10 != 0 :
    print(-1)
else :
    count_dict['A'] = n//300
    n = n-300*count_dict.get('A')

    count_dict['B'] = n // 60
    n = n - 60 * count_dict.get('B')

    count_dict['C'] = n // 10
    n = n - 10 * count_dict.get('C')

    for x in count_dict.values() :
        print(x, end=" ")



