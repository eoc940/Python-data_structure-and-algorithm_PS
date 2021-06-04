# 알파코드

import sys

code = sys.stdin.readline().rstrip()

def dfs(v, words) :
    global cnt
    if v==len(code) :
        cnt += 1
        print(words)
        return

    else :
        for i in range(1,27) :
            if code[v:].startswith(str(i)) :
                dfs(v + len(str(i)), words + chr(i+64))

cnt = 0
dfs(0, "")
print(cnt)





