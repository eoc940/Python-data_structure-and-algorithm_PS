# 쇠막대기
'''
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '{':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '{':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
'''


# 다시 풀어보기

n = input()
stack = []
cnt = 0

for i in range(len(n)) :
    if n[i]=="(" :
        stack.append(n[i])

    else : # } 이 들어왔음
        stack.pop()
        if n[i-1]==")" :
            cnt += 1
        else :
            cnt += len(stack)

print(cnt)














