# 회문 문자열 검사

import sys
n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip().lower() for _ in range(n)]
idx = 1
for word in words :

    left = 0
    right = len(word)-1
    flag = True
    while left < right :
        if word[left] == word[right] :
            left += 1
            right -= 1
        else :
            flag = False
            break
    if flag == True :
        print("#%d" %(idx), "YES")
    else :
        print("#%d" % (idx), "NO")
    idx += 1

