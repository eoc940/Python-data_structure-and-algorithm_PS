# 알파코드(DFS)
'''
def DFS(L) :
    global cnt
    if L==len(n) :
        for i in range(len(res)) :
            print(res[i], end="")
        print()
        cnt += 1
        return
    else:
        if len(n) >= L+2 and int(n[L+1])==0  :
            res.append(alpha.get(int(n[L:L + 2])))
            DFS(L + 2)
            res.pop()
        elif len(n) >= L+2 and int(n[L+1])!=0 :
            if int(n[L:L+2]) <= 26 :
                res.append(alpha.get(int(n[L])))
                DFS(L + 1)
                res.pop()
                res.append(alpha.get(int(n[L:L+2])))
                DFS(L+2)
                res.pop()
            else :
                res.append(alpha.get(int(n[L])))
                DFS(L + 1)
                res.pop()


n = input()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z']
alpha = dict()
key = 1
cnt = 0
res = []
for i in range(len(alphabet)) :
    alpha[key] = alphabet[i]
    key += 1
DFS(0)
print(cnt)


# 강사님 풀이

def DFS(L,p) :
    global cnt
    if L==n :
        cnt += 1
        for j in range(p) :
            print(chr(res[j]+64), end="")
        print()

    else :
        for i in range(1,27) :
            if code[L]==i:
                res[p] = i
                DFS(L+1,p+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[p] = i
                DFS(L+2,p+1)

code=list(map(int, input()))
n = len(code)
code.insert(n,-1) # 반복문 인덱스 처리하기 싫을 때 쓰자

alpha = dict()
key = 1
cnt = 0
res = [0]*(n+3)

DFS(0,0)
print(cnt)
'''


# 다시풀기

def DFS(L, p) :
    global cnt
    if L==n :
        for i in range(p) :
            print(chr(res[i]+64), end="")
        print()
        cnt+=1
    else :
        for i in range(1,27) :
            if code[L]==i :
                res[p] = i
                DFS(L+1, p+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10 :
                res[p] = i
                DFS(L+2, p+1)


code = list(map(int, input()))
n = len(code)
code.append(-1)
cnt = 0
res = [0]*(n+3)
DFS(0,0)
print(cnt)






































