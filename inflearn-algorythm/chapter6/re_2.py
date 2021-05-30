# 이진트리 순회(깊이우선탐색)

def dfs(v) :
    if v > 7 :
        return
    else :
        # print(v, end=" ")
        dfs(v*2)
        # print(v, end=" ")
        dfs(v*2+1)
        print(v, end=" ")

dfs(1)

